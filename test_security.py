#!/usr/bin/env python3
"""Regression checks for local-server exposure and graph XSS."""

import json
import os
import select
import signal
import socket
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
CANARY = "CANARY-SECRET-CONTENT-do-not-serve"


def listening_addresses(port):
    """Return local addresses listening on port, from /proc/net/tcp{,6}."""
    addresses = []
    for family, path in (("ipv4", "/proc/net/tcp"), ("ipv6", "/proc/net/tcp6")):
        try:
            lines = open(path, encoding="utf-8").read().splitlines()[1:]
        except FileNotFoundError:
            continue
        for line in lines:
            fields = line.split()
            local, state = fields[1], fields[3]
            if state != "0A":
                continue
            ip_hex, port_hex = local.split(":")
            if int(port_hex, 16) != port:
                continue
            addresses.append((family, ip_hex))
    return addresses


def assert_loopback_only(port):
    addresses = listening_addresses(port)
    if not addresses:
        raise AssertionError(f"nothing is listening on port {port}")
    for family, ip_hex in addresses:
        if family == "ipv4" and ip_hex == "00000000":
            raise AssertionError(f"server on {port} is bound to 0.0.0.0")
        if family == "ipv4" and ip_hex != "0100007F":
            raise AssertionError(
                f"server on {port} is bound to non-loopback IPv4 {ip_hex}"
            )
        if family == "ipv6":
            # /proc/net/tcp6 stores each 32-bit group little-endian, so ::1
            # is 00000000000000000000000001000000 and :: is all zeros.
            if set(ip_hex) == {"0"}:
                raise AssertionError(
                    f"server on {port} is bound to all IPv6 interfaces"
                )
            if ip_hex != "00000000000000000000000001000000":
                raise AssertionError(
                    f"server on {port} is bound to non-loopback IPv6 {ip_hex}"
                )


class RawResponse:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body


def raw_request(port, path):
    """Send a request path exactly, without client-side .. normalization."""
    sock = socket.create_connection(("127.0.0.1", port), timeout=5)
    try:
        sock.sendall(
            f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n".encode()
        )
        data = b""
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            data += chunk
    finally:
        sock.close()
    head, _, body = data.partition(b"\r\n\r\n")
    lines = head.decode("iso-8859-1", errors="replace").split("\r\n")
    status = int(lines[0].split()[1])
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    return RawResponse(status, headers, body)


def start_server(command):
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.Popen(
        command,
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env,
    )
    port = None
    deadline = time.time() + 8
    output = ""
    while time.time() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"{command} exited early:\n{output}")
        ready, _, _ = select.select([proc.stdout], [], [], 0.2)
        if not ready:
            continue
        line = proc.stdout.readline()
        if not line:
            continue
        output += line
        if "Server running at http://localhost:" in line:
            port = int(line.rsplit(":", 1)[1].strip().rstrip("/"))
            break
    if port is None:
        proc.send_signal(signal.SIGTERM)
        raise RuntimeError(f"could not find listen port for {command}:\n{output}")
    return proc, port


def stop_server(proc):
    if proc.poll() is None:
        proc.send_signal(signal.SIGTERM)
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=3)


def prepare_sibling_canary():
    root = os.path.realpath(REPO)
    sibling_name = os.path.basename(root) + "-secret"
    sibling = os.path.join(os.path.dirname(root), sibling_name)
    created = False
    if not os.path.isdir(sibling):
        subprocess.check_call(["sudo", "mkdir", "-p", sibling])
        created = True
    secret = os.path.join(sibling, "secret.txt")
    subprocess.run(
        ["sudo", "tee", secret],
        input=CANARY + "\n",
        text=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    subprocess.check_call(["sudo", "chmod", "a+r", secret])
    return sibling_name, secret, created


def cleanup_sibling(secret, created, sibling_name):
    subprocess.call(["sudo", "rm", "-f", secret])
    if created:
        sibling = os.path.join(os.path.dirname(os.path.realpath(REPO)), sibling_name)
        subprocess.call(["sudo", "rmdir", sibling])


def check_server(name, command):
    sibling_name, secret, created = prepare_sibling_canary()
    proc, port = start_server(command)
    try:
        assert_loopback_only(port)

        page = raw_request(port, "/knowledge-graph.html")
        if page.status != 200 or b"mynetwork" not in page.body:
            raise AssertionError(
                f"{name} did not serve knowledge-graph.html ({page.status})"
            )

        data = raw_request(port, "/knowledge-graph.json")
        if data.status != 200 or b'"nodes"' not in data.body:
            raise AssertionError(
                f"{name} did not serve knowledge-graph.json ({data.status})"
            )

        origin = data.headers.get("access-control-allow-origin")
        if origin is not None:
            raise AssertionError(
                f"{name} still sends Access-Control-Allow-Origin: {origin}"
            )

        git = raw_request(port, "/.git/config")
        if git.status != 403:
            raise AssertionError(f"{name} served /.git/config with status {git.status}")

        hidden = raw_request(port, "/.gitignore")
        if hidden.status != 403:
            raise AssertionError(
                f"{name} served /.gitignore with status {hidden.status}"
            )

        traversal = raw_request(port, f"/../{sibling_name}/secret.txt")
        if CANARY.encode() in traversal.body or traversal.status == 200:
            raise AssertionError(
                f"{name} leaked a sibling file via prefix bypass (status {traversal.status})"
            )
        if traversal.status != 403:
            raise AssertionError(
                f"{name} traversal status was {traversal.status}, expected 403"
            )

        encoded = raw_request(port, f"/%2e%2e/{sibling_name}/secret.txt")
        if CANARY.encode() in encoded.body or encoded.status == 200:
            raise AssertionError(f"{name} leaked a sibling file via encoded traversal")
        if encoded.status != 403:
            raise AssertionError(
                f"{name} encoded traversal status was {encoded.status}, expected 403"
            )

        print(f"PASS {name} (port {port})")
    finally:
        stop_server(proc)
        cleanup_sibling(secret, created, sibling_name)


def check_script_sri():
    html = open(os.path.join(REPO, "knowledge-graph.html"), encoding="utf-8").read()
    needle = "https://unpkg.com/vis-network@9.1.9/dist/vis-network.min.js"
    if needle not in html:
        raise AssertionError("vis-network script URL missing")
    if 'integrity="sha384-' not in html or 'crossorigin="anonymous"' not in html:
        raise AssertionError("vis-network script is loaded without SRI")
    print("PASS script SRI attribute present")


def check_browser():
    from playwright.sync_api import sync_playwright

    check_script_sri()
    proc, port = start_server([sys.executable, "server.py"])
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.add_init_script("window.__xss = 0;")

            def fulfill_graph(route):
                payload = json.loads(
                    open(
                        os.path.join(REPO, "knowledge-graph.json"), encoding="utf-8"
                    ).read()
                )
                payload["nodes"].append(
                    {
                        "id": "xss-label",
                        "label": '<img src=x onerror="window.__xss=1">',
                        "type": "person",
                        "date": "<script>window.__xss=1</script>",
                        "references": [
                            '1 Nephi 1:1"><img src=x onerror="window.__xss=1">'
                        ],
                    }
                )
                payload["nodes"].append(
                    {
                        "id": "x');window.__xss=1;//",
                        "label": "XSSIDNODE",
                        "type": "person",
                        "references": ["1 Nephi 1:1"],
                    }
                )
                payload["edges"].append(
                    {
                        "from": "Nephi",
                        "to": "x');window.__xss=1;//",
                        "label": "sibling_of",
                        "references": ["1 Nephi 1:1"],
                    }
                )
                route.fulfill(
                    status=200,
                    content_type="application/json",
                    body=json.dumps(payload),
                )

            page.route("**/knowledge-graph.json", fulfill_graph)
            page.goto(
                f"http://127.0.0.1:{port}/knowledge-graph.html",
                wait_until="networkidle",
            )
            page.wait_for_selector("#mynetwork canvas", timeout=15000)
            box = page.query_selector("#mynetwork canvas").bounding_box()
            if not box or box["width"] < 50 or box["height"] < 50:
                raise AssertionError(f"graph canvas did not render: {box}")

            page.fill("#searchInput", "nephi")
            page.wait_for_function(
                "() => document.querySelectorAll('#searchResults div').length > 0"
            )

            page.fill("#searchInput", "<img")
            page.wait_for_selector("#searchResults div")
            page.click("#searchResults div")
            page.wait_for_timeout(300)
            xss_count = page.evaluate("() => window.__xss")
            if xss_count:
                raise AssertionError(
                    "untrusted graph fields executed script in the details pane"
                )
            details = page.inner_text("#detailsContent")
            if "<img" not in details or "onerror" not in details:
                raise AssertionError(
                    f"malicious label was not shown as text: {details!r}"
                )
            if page.query_selector("#detailsContent img"):
                raise AssertionError(
                    "details pane created an image element from node data"
                )

            # Selecting Nephi renders the malicious neighbor id inside a chip.
            page.evaluate("() => { window.__xss = 0; }")
            page.fill("#searchInput", "Nephi")
            page.evaluate("""() => {
                  const el = [...document.querySelectorAll('#searchResults div')]
                    .find((node) => node.textContent === 'Nephi');
                  if (!el) throw new Error('Nephi search result missing');
                  el.click();
                }""")
            page.wait_for_timeout(300)
            page.locator("#detailsContent span", has_text="XSSIDNODE").click()
            page.wait_for_timeout(300)
            if page.evaluate("() => window.__xss"):
                raise AssertionError("connected-node id broke out of the click handler")

            page.select_option("#edgeFilter", "parent_of")
            page.wait_for_timeout(200)
            print("PASS browser graph render and XSS containment")
            browser.close()
    finally:
        stop_server(proc)


def main():
    failures = []
    checks = [
        lambda: check_server("python", [sys.executable, "server.py"]),
        lambda: check_server("node", ["node", "server.js"]),
        check_script_sri,
    ]
    if "--browser" in sys.argv:
        checks.append(check_browser)
    for check in checks:
        try:
            check()
        except Exception as exc:
            failures.append(str(exc))
            print(f"FAIL {exc}")
    if failures:
        print(f"\n{len(failures)} security check(s) failed")
        return 1
    print("\nAll security checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

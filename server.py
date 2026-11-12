#!/usr/bin/env python3
"""
Loopback static server for the knowledge graph.

The HTML page and knowledge-graph.json are served from this directory on
the same origin, so cross-origin reads are not enabled. Hidden files
(including .git) and paths outside this directory are refused.
"""

import errno
import http.server
import os
import socket
import socketserver
import sys
import threading
import urllib.parse

PORT = 8000


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _path_allowed(self):
        decoded = urllib.parse.unquote(urllib.parse.urlparse(self.path).path)
        if "\x00" in decoded:
            return False

        parts = []
        for part in decoded.split("/"):
            if part in ("", "."):
                continue
            # Reject parent traversal and dotfiles such as .git/config.
            if part == ".." or part.startswith("."):
                return False
            parts.append(part)

        root = os.path.realpath(os.getcwd())
        candidate = os.path.realpath(os.path.join(root, *parts))
        try:
            inside = os.path.commonpath([root, candidate]) == root
        except ValueError:
            return False
        return inside

    def do_GET(self):
        if not self._path_allowed():
            self.send_error(403, "Forbidden")
            return
        super().do_GET()

    def do_HEAD(self):
        if not self._path_allowed():
            self.send_error(403, "Forbidden")
            return
        super().do_HEAD()


def _bind(family, address, port):
    class BoundServer(socketserver.TCPServer):
        allow_reuse_address = True
        address_family = family

    return BoundServer((address, port), MyHTTPRequestHandler)


def serve(port):
    servers = [_bind(socket.AF_INET, "127.0.0.1", port)]

    try:
        servers.append(_bind(socket.AF_INET6, "::1", port))
    except OSError as exc:
        print(f"IPv6 loopback unavailable ({exc}); continuing on 127.0.0.1")

    print(f"Server running at http://localhost:{port}/")
    print(f"Open http://localhost:{port}/knowledge-graph.html in your browser")
    print("Press Ctrl+C to stop the server")

    threads = []
    for extra in servers[1:]:
        thread = threading.Thread(target=extra.serve_forever, daemon=True)
        thread.start()
        threads.append(thread)

    try:
        servers[0].serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        for httpd in servers:
            httpd.shutdown()
            httpd.server_close()


if __name__ == "__main__":
    try:
        serve(PORT)
    except OSError as exc:
        if exc.errno == errno.EADDRINUSE:
            print(f"Port {PORT} is already in use. Trying port {PORT + 1}...")
            try:
                serve(PORT + 1)
            except OSError as next_exc:
                print(f"Error starting server: {next_exc}")
                sys.exit(1)
        else:
            print(f"Error starting server: {exc}")
            sys.exit(1)

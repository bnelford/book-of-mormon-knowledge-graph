#!/usr/bin/env python3
"""
Simple HTTP server to serve the knowledge graph files locally.
This resolves CORS issues when loading JSON data in the browser.
"""

import http.server
import socketserver
import os
import sys

# Change to the directory containing the HTML file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow loading JSON files
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}/")
            print(f"Open http://localhost:{PORT}/knowledge-graph.html in your browser")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Port {PORT} is already in use. Trying port {PORT + 1}...")
            PORT += 1
            with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
                print(f"Server running at http://localhost:{PORT}/")
                print(f"Open http://localhost:{PORT}/knowledge-graph.html in your browser")
                print("Press Ctrl+C to stop the server")
                httpd.serve_forever()
        else:
            print(f"Error starting server: {e}")
            sys.exit(1)

"""Minimal HTTP service used to demonstrate CI/CD failure prediction.

Intentionally trivial — the only thing being predicted is the CI build
outcome, not behaviour at runtime.
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"hello from demo\n")


def main(port: int = 8080) -> None:
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"serving on http://0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()

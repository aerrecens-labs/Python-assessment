from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import os
import re

from tasks import get_tasks, toggle_task

PORT = int(os.environ.get("PORT", "3000"))


class TaskHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, body) -> None:
        payload = b"" if body is None else json.dumps(body).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, PATCH, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if payload:
            self.wfile.write(payload)

    def do_OPTIONS(self) -> None:
        self._send_json(204, None)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._send_json(200, {"ok": True})
            return

        if parsed.path == "/tasks":
            query = parse_qs(parsed.query)
            status = query.get("status", ["all"])[0]
            self._send_json(200, get_tasks(status))
            return

        self._send_json(404, {"error": "Not found"})

    def do_PATCH(self) -> None:
        match = re.fullmatch(r"/tasks/(\d+)/toggle", urlparse(self.path).path)
        if not match:
            self._send_json(404, {"error": "Not found"})
            return

        task = toggle_task(int(match.group(1)))
        if task is None:
            self._send_json(404, {"error": "Task not found"})
            return

        self._send_json(200, task)

    def log_message(self, format: str, *args) -> None:
        print("%s - %s" % (self.address_string(), format % args))


def main() -> None:
    server = HTTPServer(("127.0.0.1", PORT), TaskHandler)
    print(f"Task API listening on http://localhost:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()

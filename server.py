import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


parser = argparse.ArgumentParser()
parser.add_argument("--commit-label", required=True)
args = parser.parse_args()

launch_evidence = {
    "commit_label": args.commit_label,
    "argv": list(sys.argv),
    "cwd": os.getcwd(),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._send(200, "ok")
        elif self.path == "/":
            self._send(200, args.commit_label)
        elif self.path == "/evidence":
            self._send(
                200,
                json.dumps(launch_evidence, separators=(",", ":")),
                "application/json",
            )
        else:
            self._send(404, "not found")

    def _send(self, status, body, content_type="text/plain; charset=utf-8"):
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        pass


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

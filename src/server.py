from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routes.task_routes import TaskRoutes
from config import PORT

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/tasks"):
            response = TaskRoutes.get_tasks()
            self._send(response)
        else:
            self._send({"error": "Not found"}, 404)

    def do_POST(self):
        if self.path == "/tasks":
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            data = json.loads(body)
            response = TaskRoutes.create_task(data)
            self._send(response)
        else:
            self._send({"error": "Not found"}, 404)

    def _send(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == "__main__":
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("localhost", PORT), Server)
    server.serve_forever()
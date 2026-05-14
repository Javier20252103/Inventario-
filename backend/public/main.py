from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class AppHandler(BaseHTTPRequestHandler):

    def send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/health":
            response = {
                "success": True,
                "message": "Backend InventoryPro funcionando correctamente",
                "data": {
                    "status": "ok",
                    "project": "InventoryPro",
                    "backend": "Python sin framework"
                }
            }
            self.send_json_response(200, response)
        else:
            response = {
                "success": False,
                "message": "Ruta no encontrada",
                "error": {
                    "code": "ROUTE_NOT_FOUND",
                    "details": []
                }
            }
            self.send_json_response(404, response)


def run_server():
    host = "localhost"
    port = 8000

    server = HTTPServer((host, port), AppHandler)
    print(f"Servidor corriendo en http://{host}:{port}")
    print(f"Health check: http://{host}:{port}/api/health")

    server.serve_forever()


if __name__ == "__main__":
    run_server()
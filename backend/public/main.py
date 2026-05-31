from http.server import BaseHTTPRequestHandler, HTTPServer
import json


products = [
    {
        "id": 1,
        "code": "P-001",
        "name": "Laptop Lenovo",
        "category": "Electrónica",
        "supplier": "TecnoMax",
        "minimum_stock": 5,
        "status": "Activo"
    },
    {
        "id": 2,
        "code": "P-002",
        "name": "Mouse Logitech",
        "category": "Accesorios",
        "supplier": "CompuCenter",
        "minimum_stock": 10,
        "status": "Activo"
    },
    {
        "id": 3,
        "code": "P-003",
        "name": "Teclado Mecánico",
        "category": "Accesorios",
        "supplier": "Digital Store",
        "minimum_stock": 7,
        "status": "Activo"
    }
]

stock = [
    {
        "product_id": 1,
        "product": "Laptop Lenovo",
        "warehouse": "Almacén principal",
        "current_stock": 12,
        "status": "Disponible"
    },
    {
        "product_id": 2,
        "product": "Mouse Logitech",
        "warehouse": "Almacén principal",
        "current_stock": 4,
        "status": "Stock bajo"
    },
    {
        "product_id": 3,
        "product": "Teclado Mecánico",
        "warehouse": "Almacén secundario",
        "current_stock": 18,
        "status": "Disponible"
    }
]

movements = [
    {
        "id": 1,
        "type": "Entrada",
        "product": "Laptop Lenovo",
        "quantity": 10,
        "user": "Juan Manuel",
        "date": "21/05/2026"
    },
    {
        "id": 2,
        "type": "Salida",
        "product": "Mouse Logitech",
        "quantity": 3,
        "user": "Juan Manuel",
        "date": "21/05/2026"
    },
    {
        "id": 3,
        "type": "Entrada",
        "product": "Teclado Mecánico",
        "quantity": 15,
        "user": "Juan Manuel",
        "date": "21/05/2026"
    }
]


class AppHandler(BaseHTTPRequestHandler):

    def send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

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

        elif self.path == "/api/dashboard/summary":
            response = {
                "success": True,
                "message": "Resumen del dashboard obtenido correctamente",
                "data": {
                    "clients": 16,
                    "suppliers": 10,
                    "products": 185,
                    "invoices": 1,
                    "total_stock": 149,
                    "sold_stock": 33,
                    "current_stock": 115,
                    "amount_sold": 413,
                    "amount_paid": 413,
                    "remaining_amount": 0,
                    "gross_profit": 89,
                    "net_profit": 89
                }
            }
            self.send_json_response(200, response)

        elif self.path == "/api/products":
            response = {
                "success": True,
                "message": "Productos obtenidos correctamente",
                "data": products
            }
            self.send_json_response(200, response)

        elif self.path == "/api/inventory/stock":
            response = {
                "success": True,
                "message": "Stock obtenido correctamente",
                "data": stock
            }
            self.send_json_response(200, response)

        elif self.path == "/api/inventory/movements":
            response = {
                "success": True,
                "message": "Movimientos obtenidos correctamente",
                "data": movements
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
    print(f"Dashboard: http://{host}:{port}/api/dashboard/summary")
    print(f"Productos: http://{host}:{port}/api/products")
    print(f"Stock: http://{host}:{port}/api/inventory/stock")
    print(f"Movimientos: http://{host}:{port}/api/inventory/movements")

    server.serve_forever()


if __name__ == "__main__":
    run_server()
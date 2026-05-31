"""
Avance mínimo: un solo GET que lee un documento en Firestore.
Colección/documento por defecto: avance/demo (configurable con FIRESTORE_DOC_PATH).
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

_backend_dir = Path(__file__).resolve().parents[1]
load_dotenv(_backend_dir / ".env")

FRONTEND_ORIGIN = os.environ.get("FRONTEND_ORIGIN", "http://localhost:5173").strip()
PORT = int(os.environ.get("PORT", "8000"))
FIREBASE_CREDENTIALS_PATH = os.environ.get("FIREBASE_CREDENTIALS_PATH", "").strip()
# Ruta del documento en Firestore, ej. "avance/demo"
FIRESTORE_DOC_PATH = os.environ.get("FIRESTORE_DOC_PATH", "avance/demo").strip()

_db = None


def _get_db():
    global _db
    if _db is not None:
        return _db
    import firebase_admin
    from firebase_admin import credentials, firestore

    if not FIREBASE_CREDENTIALS_PATH or not Path(FIREBASE_CREDENTIALS_PATH).is_file():
        raise RuntimeError(
            "Configura FIREBASE_CREDENTIALS_PATH en backend/.env apuntando al JSON de servicio."
        )
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)
    _db = firestore.client()
    return _db


def _read_avance_doc():
    db = _get_db()
    doc_ref = db.document(FIRESTORE_DOC_PATH)
    snap = doc_ref.get()
    if not snap.exists:
        return None, "El documento no existe en Firestore (créalo en la consola)."
    return snap.to_dict(), None


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
    def log_message(self, format, *args):
        return

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", FRONTEND_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Credentials", "true")

    def send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._cors()
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
<<<<<<< HEAD
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
=======
        self.wfile.write(body)
>>>>>>> origin/gioauth-firebase

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
<<<<<<< HEAD
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
=======
        path = self.path.split("?", 1)[0]
        if path == "/api/health":
            self.send_json(
                200,
                {
                    "success": True,
                    "message": "Backend InventoryPro OK",
                    "data": {"status": "ok"},
                },
            )
            return
        if path == "/api/avance":
            try:
                data, err = _read_avance_doc()
                if err:
                    self.send_json(
                        200,
                        {
                            "success": True,
                            "message": "Conexión a Firestore OK; falta el documento de demo.",
                            "data": {
                                "firestore_path": FIRESTORE_DOC_PATH,
                                "hint": err,
                                "payload": None,
                            },
                        },
                    )
                    return
                self.send_json(
                    200,
                    {
                        "success": True,
                        "message": "Lectura desde Firestore correcta.",
                        "data": {
                            "firestore_path": FIRESTORE_DOC_PATH,
                            "payload": _serialize_firestore(data),
                        },
                    },
                )
            except Exception:
                self.send_json(
                    500,
                    {
                        "success": False,
                        "message": "No se pudo leer Firestore. Revisa credenciales y reglas.",
                        "error": {"code": "FIRESTORE_ERROR", "details": []},
                    },
                )
            return

        self.send_json(
            404,
            {
>>>>>>> origin/gioauth-firebase
                "success": False,
                "message": "Ruta no encontrada",
                "error": {"code": "ROUTE_NOT_FOUND", "details": []},
            },
        )


def _serialize_firestore(value):
    if value is None:
        return None
    if hasattr(value, "isoformat"):
        try:
            return value.isoformat()
        except Exception:
            return str(value)
    if isinstance(value, dict):
        return {k: _serialize_firestore(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_serialize_firestore(v) for v in value]
    return value


def run_server():
<<<<<<< HEAD
    host = "localhost"
    port = 8000

    server = HTTPServer((host, port), AppHandler)
    print(f"Servidor corriendo en http://{host}:{port}")
    print(f"Health check: http://{host}:{port}/api/health")
    print(f"Dashboard: http://{host}:{port}/api/dashboard/summary")
    print(f"Productos: http://{host}:{port}/api/products")
    print(f"Stock: http://{host}:{port}/api/inventory/stock")
    print(f"Movimientos: http://{host}:{port}/api/inventory/movements")

=======
    host = "0.0.0.0"
    server = HTTPServer((host, PORT), AppHandler)
    print(f"API: http://localhost:{PORT}/api/avance (lee Firestore: {FIRESTORE_DOC_PATH})")
    print(f"CORS solo para: {FRONTEND_ORIGIN}")
>>>>>>> origin/gioauth-firebase
    server.serve_forever()


if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        sys.exit(0)

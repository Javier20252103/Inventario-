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
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
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
    host = "0.0.0.0"
    server = HTTPServer((host, PORT), AppHandler)
    print(f"API: http://localhost:{PORT}/api/avance (lee Firestore: {FIRESTORE_DOC_PATH})")
    print(f"CORS solo para: {FRONTEND_ORIGIN}")
    server.serve_forever()


if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        sys.exit(0)

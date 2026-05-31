import sys
from pathlib import Path

from flask import Flask, jsonify

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.middlewares.cors import configure_cors
from src.routes.auth import auth_bp
from src.routes.crud import crud_bp
from src.config.env import Config


def create_app():
    app = Flask(__name__)

    configure_cors(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(crud_bp, url_prefix="/api")

    @app.get("/")
    def home():
        return jsonify({
            "message": "InventoryPro Backend en Python funcionando",
            "status": "ok"
        }), 200

    @app.get("/api/health")
    def health():
        return jsonify({
            "message": "Backend funcionando correctamente",
            "status": "ok"
        }), 200

    return app


app = create_app()


if __name__ == "__main__":
    print(f"🚀 InventoryPro backend corriendo en http://localhost:{Config.PORT}")
    app.run(host="0.0.0.0", port=Config.PORT, debug=True)        
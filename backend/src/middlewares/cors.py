from flask_cors import CORS
from src.config.env import Config


def configure_cors(app):
    CORS(
        app,
        resources={r"/api/*": {"origins": Config.CORS_ORIGIN}},
        supports_credentials=True
    )  
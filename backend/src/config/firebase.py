import firebase_admin
from firebase_admin import credentials, firestore
from src.config.env import Config


_db = None


def init_firebase():
    global _db

    if _db is not None:
        return _db

    if not Config.FIREBASE_PROJECT_ID:
        print("⚠️ Firebase no configurado. Revisa tu archivo .env")
        return None

    private_key = Config.FIREBASE_PRIVATE_KEY

    if private_key:
        private_key = private_key.replace("\\n", "\n")

    firebase_credentials = {
        "type": "service_account",
        "project_id": Config.FIREBASE_PROJECT_ID,
        "private_key": private_key,
        "client_email": Config.FIREBASE_CLIENT_EMAIL,
        "token_uri": Config.FIREBASE_TOKEN_URI,
    }

    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_credentials)
        firebase_admin.initialize_app(cred)

    _db = firestore.client()
    return _db


def get_db():
    return init_firebase()   
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT = int(os.getenv("PORT", 8000))
    CORS_ORIGIN = os.getenv("CORS_ORIGIN", "*")

    FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
    FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL")
    FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY")
    FIREBASE_TOKEN_URI = os.getenv(
        "FIREBASE_TOKEN_URI",
        "https://oauth2.googleapis.com/token"
    )
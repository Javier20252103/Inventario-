from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.services.firestore_service import FirestoreService

auth_bp = Blueprint("auth", __name__)

users_service = FirestoreService("usuarios")


@auth_bp.post("/register")
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")
    rol = data.get("rol", "usuario")

    if not nombre or not email or not password:
        return jsonify({
            "error": "Nombre, email y password son obligatorios"
        }), 400

    usuarios = users_service.get_all()

    for usuario in usuarios:
        if usuario.get("email") == email:
            return jsonify({"error": "El correo ya está registrado"}), 400

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "password": generate_password_hash(password),
        "rol": rol,
        "activo": True
    }

    usuario_creado = users_service.create(nuevo_usuario)
    usuario_creado.pop("password", None)

    return jsonify({
        "message": "Usuario registrado correctamente",
        "usuario": usuario_creado
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email y password son obligatorios"
        }), 400

    usuarios = users_service.get_all()

    usuario_encontrado = None

    for usuario in usuarios:
        if usuario.get("email") == email:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        return jsonify({"error": "Credenciales incorrectas"}), 401

    password_guardado = usuario_encontrado.get("password")

    if not check_password_hash(password_guardado, password):
        return jsonify({"error": "Credenciales incorrectas"}), 401

    usuario_encontrado.pop("password", None)

    return jsonify({
        "message": "Inicio de sesión correcto",
        "usuario": usuario_encontrado
    }), 200


@auth_bp.post("/logout")
def logout():
    return jsonify({
        "message": "Sesión cerrada correctamente"
    }), 200   
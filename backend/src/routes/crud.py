from flask import Blueprint, request, jsonify
from src.services.firestore_service import FirestoreService

crud_bp = Blueprint("crud", __name__)

COLLECTIONS_ALLOWED = [
    "productos",
    "categorias",
    "proveedores",
    "usuarios"
]


def get_service(collection):
    if collection not in COLLECTIONS_ALLOWED:
        return None
    return FirestoreService(collection)


@crud_bp.get("/<collection>")
def get_all(collection):
    service = get_service(collection)

    if service is None:
        return jsonify({"error": "Colección no permitida"}), 400

    try:
        data = service.get_all()
        return jsonify({
            "message": f"Listado de {collection}",
            "data": data
        }), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@crud_bp.get("/<collection>/<document_id>")
def get_by_id(collection, document_id):
    service = get_service(collection)

    if service is None:
        return jsonify({"error": "Colección no permitida"}), 400

    try:
        item = service.get_by_id(document_id)

        if item is None:
            return jsonify({"error": "Registro no encontrado"}), 404

        return jsonify({
            "message": "Registro encontrado",
            "data": item
        }), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@crud_bp.post("/<collection>")
def create(collection):
    service = get_service(collection)

    if service is None:
        return jsonify({"error": "Colección no permitida"}), 400

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    try:
        item = service.create(data)

        return jsonify({
            "message": "Registro creado correctamente",
            "data": item
        }), 201
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@crud_bp.put("/<collection>/<document_id>")
def update(collection, document_id):
    service = get_service(collection)

    if service is None:
        return jsonify({"error": "Colección no permitida"}), 400

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    try:
        item = service.update(document_id, data)

        if item is None:
            return jsonify({"error": "Registro no encontrado"}), 404

        return jsonify({
            "message": "Registro actualizado correctamente",
            "data": item
        }), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@crud_bp.delete("/<collection>/<document_id>")
def delete(collection, document_id):
    service = get_service(collection)

    if service is None:
        return jsonify({"error": "Colección no permitida"}), 400

    try:
        deleted = service.delete(document_id)

        if not deleted:
            return jsonify({"error": "Registro no encontrado"}), 404

        return jsonify({
            "message": "Registro eliminado correctamente"
        }), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500   
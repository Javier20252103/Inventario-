producto_schema = {
    "nombre": str,
    "descripcion": str,
    "precio": float,
    "stock": int,
    "categoria_id": str,
    "proveedor_id": str
}

categoria_schema = {
    "nombre": str,
    "descripcion": str
}

proveedor_schema = {
    "nombre": str,
    "telefono": str,
    "email": str,
    "direccion": str
}

usuario_schema = {
    "nombre": str,
    "email": str,
    "password": str,
    "rol": str
}  
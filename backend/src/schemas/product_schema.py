# Esquema de productos
# Valida que los datos lleguen correctos antes de procesarlos

def validate_product(data):
    """
    Valida los datos de un producto.
    Regresa una lista de errores, o lista vacía si todo está bien.
    """
    errors = []

    if not data.get("name"):
        errors.append("El nombre es obligatorio")
    elif len(data["name"]) > 100:
        errors.append("El nombre no puede tener más de 100 caracteres")

    if data.get("price") is None:
        errors.append("El precio es obligatorio")
    elif data["price"] < 0:
        errors.append("El precio no puede ser negativo")

    if data.get("stock") is not None and data["stock"] < 0:
        errors.append("El stock no puede ser negativo")

    if not data.get("category_id"):
        errors.append("La categoría es obligatoria")

    return errors

# Esquema de categorías
# Valida que los datos lleguen correctos antes de procesarlos

def validate_category(data):
    """
    Valida los datos de una categoría.
    Regresa una lista de errores, o lista vacía si todo está bien.
    """
    errors = []

    if not data.get("name"):
        errors.append("El nombre es obligatorio")
    elif len(data["name"]) > 50:
        errors.append("El nombre no puede tener más de 50 caracteres")

    if data.get("description") and len(data["description"]) > 200:
        errors.append("La descripción no puede tener más de 200 caracteres")

    return errors

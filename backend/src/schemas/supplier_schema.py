# Esquema de proveedores
# Valida que los datos lleguen correctos antes de procesarlos

def validate_supplier(data):
    """
    Valida los datos de un proveedor.
    Regresa una lista de errores, o lista vacía si todo está bien.
    """
    errors = []

    if not data.get("name"):
        errors.append("El nombre es obligatorio")
    elif len(data["name"]) > 100:
        errors.append("El nombre no puede tener más de 100 caracteres")

    if not data.get("contact_email"):
        errors.append("El correo de contacto es obligatorio")

    if data.get("phone") and len(data["phone"]) > 20:
        errors.append("El teléfono no puede tener más de 20 caracteres")

    return errors

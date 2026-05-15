# Rutas de proveedores
# Define las URLs disponibles y las conecta al controlador

from controllers.supplier_controller import SupplierController

controller = SupplierController()

def register_supplier_routes(handler):
    """Registra las rutas de proveedores en el servidor."""
    routes = {
        "GET /api/suppliers":        controller.get_all,
        "POST /api/suppliers":       controller.create,
        "PUT /api/suppliers/:id":    controller.update,
        "DELETE /api/suppliers/:id": controller.delete,
    }
    return routes

# Rutas de categorías
# Define las URLs disponibles y las conecta al controlador

from controllers.category_controller import CategoryController

controller = CategoryController()

def register_category_routes(handler):
    """Registra las rutas de categorías en el servidor."""
    routes = {
        "GET /api/categories":        controller.get_all,
        "POST /api/categories":       controller.create,
        "PUT /api/categories/:id":    controller.update,
        "DELETE /api/categories/:id": controller.delete,
    }
    return routes

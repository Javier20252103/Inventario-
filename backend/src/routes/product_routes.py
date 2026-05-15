# Rutas de productos
# Define las URLs disponibles y las conecta al controlador

from controllers.product_controller import ProductController

controller = ProductController()

def register_product_routes(handler):
    """Registra las rutas de productos en el servidor."""
    routes = {
        "GET /api/products":              controller.get_all,
        "POST /api/products":             controller.create,
        "PUT /api/products/:id":          controller.update,
        "PATCH /api/products/:id/status": controller.change_status,
        "DELETE /api/products/:id":       controller.delete,
    }
    return routes

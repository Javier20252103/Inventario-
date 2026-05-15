# Controlador de productos
# Recibe la petición, llama al servicio y devuelve la respuesta JSON

from services.product_service import ProductService

class ProductController:

    def __init__(self):
        self.service = ProductService()

    def get_all(self, handler):
        """GET /api/products — Obtiene todos los productos"""
        data = self.service.get_all()
        return {"success": True, "data": data}

    def create(self, handler, body):
        """POST /api/products — Crea un nuevo producto"""
        result = self.service.create(body)
        return {"success": True, "data": result}

    def update(self, handler, product_id, body):
        """PUT /api/products/:id — Actualiza un producto"""
        result = self.service.update(product_id, body)
        return {"success": True, "data": result}

    def change_status(self, handler, product_id, body):
        """PATCH /api/products/:id/status — Cambia el estatus del producto"""
        result = self.service.change_status(product_id, body)
        return {"success": True, "data": result}

    def delete(self, handler, product_id):
        """DELETE /api/products/:id — Baja lógica del producto"""
        self.service.delete(product_id)
        return {"success": True, "message": "Producto eliminado"}

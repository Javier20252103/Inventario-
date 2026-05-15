# Controlador de categorías
# Recibe la petición, llama al servicio y devuelve la respuesta JSON

from services.category_service import CategoryService

class CategoryController:

    def __init__(self):
        self.service = CategoryService()

    def get_all(self, handler):
        """GET /api/categories — Obtiene todas las categorías"""
        data = self.service.get_all()
        return {"success": True, "data": data}

    def create(self, handler, body):
        """POST /api/categories — Crea una nueva categoría"""
        result = self.service.create(body)
        return {"success": True, "data": result}

    def update(self, handler, category_id, body):
        """PUT /api/categories/:id — Actualiza una categoría"""
        result = self.service.update(category_id, body)
        return {"success": True, "data": result}

    def delete(self, handler, category_id):
        """DELETE /api/categories/:id — Elimina una categoría"""
        self.service.delete(category_id)
        return {"success": True, "message": "Categoría eliminada"}

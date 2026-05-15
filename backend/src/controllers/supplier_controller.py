# Controlador de proveedores
# Recibe la petición, llama al servicio y devuelve la respuesta JSON

from services.supplier_service import SupplierService

class SupplierController:

    def __init__(self):
        self.service = SupplierService()

    def get_all(self, handler):
        """GET /api/suppliers — Obtiene todos los proveedores"""
        data = self.service.get_all()
        return {"success": True, "data": data}

    def create(self, handler, body):
        """POST /api/suppliers — Crea un nuevo proveedor"""
        result = self.service.create(body)
        return {"success": True, "data": result}

    def update(self, handler, supplier_id, body):
        """PUT /api/suppliers/:id — Actualiza un proveedor"""
        result = self.service.update(supplier_id, body)
        return {"success": True, "data": result}

    def delete(self, handler, supplier_id):
        """DELETE /api/suppliers/:id — Elimina un proveedor"""
        self.service.delete(supplier_id)
        return {"success": True, "message": "Proveedor eliminado"}

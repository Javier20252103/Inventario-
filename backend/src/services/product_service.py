# Servicio de productos
# Aquí vive la lógica del negocio

from repositories.product_repository import ProductRepository
from schemas.product_schema import validate_product

class ProductService:

    def __init__(self):
        self.repo = ProductRepository()

    def get_all(self):
        return self.repo.find_all()

    def create(self, data):
        errors = validate_product(data)
        if errors:
            raise ValueError(errors)
        return self.repo.save(data)

    def update(self, product_id, data):
        errors = validate_product(data)
        if errors:
            raise ValueError(errors)
        return self.repo.update(product_id, data)

    def change_status(self, product_id, data):
        if "status" not in data:
            raise ValueError("El campo 'status' es requerido")
        return self.repo.update_status(product_id, data["status"])

    def delete(self, product_id):
        # Baja lógica: cambia el status en lugar de borrar
        return self.repo.update_status(product_id, "inactivo")

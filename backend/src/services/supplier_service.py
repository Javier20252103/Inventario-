# Servicio de proveedores
# Aquí vive la lógica del negocio

from repositories.supplier_repository import SupplierRepository
from schemas.supplier_schema import validate_supplier

class SupplierService:

    def __init__(self):
        self.repo = SupplierRepository()

    def get_all(self):
        return self.repo.find_all()

    def create(self, data):
        errors = validate_supplier(data)
        if errors:
            raise ValueError(errors)
        return self.repo.save(data)

    def update(self, supplier_id, data):
        errors = validate_supplier(data)
        if errors:
            raise ValueError(errors)
        return self.repo.update(supplier_id, data)

    def delete(self, supplier_id):
        return self.repo.delete(supplier_id)

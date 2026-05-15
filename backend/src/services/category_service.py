# Servicio de categorías
# Aquí vive la lógica del negocio

from repositories.category_repository import CategoryRepository
from schemas.category_schema import validate_category

class CategoryService:

    def __init__(self):
        self.repo = CategoryRepository()

    def get_all(self):
        return self.repo.find_all()

    def create(self, data):
        # Validar los datos antes de guardar
        errors = validate_category(data)
        if errors:
            raise ValueError(errors)
        return self.repo.save(data)

    def update(self, category_id, data):
        errors = validate_category(data)
        if errors:
            raise ValueError(errors)
        return self.repo.update(category_id, data)

    def delete(self, category_id):
        return self.repo.delete(category_id)

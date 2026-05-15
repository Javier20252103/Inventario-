# Repositorio de categorías
# El único que habla con la base de datos

class CategoryRepository:

    def find_all(self):
        """Obtiene todas las categorías de la base de datos"""
        # TODO: conectar con la base de datos real
        return []

    def save(self, data):
        """Inserta una nueva categoría"""
        # TODO: INSERT INTO categories
        return data

    def update(self, category_id, data):
        """Actualiza una categoría por ID"""
        # TODO: UPDATE categories SET ... WHERE id = category_id
        return data

    def delete(self, category_id):
        """Elimina una categoría por ID"""
        # TODO: DELETE FROM categories WHERE id = category_id
        return True

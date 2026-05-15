# Repositorio de productos
# El único que habla con la base de datos

class ProductRepository:

    def find_all(self):
        """Obtiene todos los productos de la base de datos"""
        # TODO: conectar con la base de datos real
        return []

    def save(self, data):
        """Inserta un nuevo producto"""
        # TODO: INSERT INTO products
        return data

    def update(self, product_id, data):
        """Actualiza un producto por ID"""
        # TODO: UPDATE products SET ... WHERE id = product_id
        return data

    def update_status(self, product_id, status):
        """Cambia el estatus de un producto"""
        # TODO: UPDATE products SET status = ? WHERE id = product_id
        return {"id": product_id, "status": status}

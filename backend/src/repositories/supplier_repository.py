# Repositorio de proveedores
# El único que habla con la base de datos

class SupplierRepository:

    def find_all(self):
        """Obtiene todos los proveedores de la base de datos"""
        # TODO: conectar con la base de datos real
        return []

    def save(self, data):
        """Inserta un nuevo proveedor"""
        # TODO: INSERT INTO suppliers
        return data

    def update(self, supplier_id, data):
        """Actualiza un proveedor por ID"""
        # TODO: UPDATE suppliers SET ... WHERE id = supplier_id
        return data

    def delete(self, supplier_id):
        """Elimina un proveedor por ID"""
        # TODO: DELETE FROM suppliers WHERE id = supplier_id
        return True

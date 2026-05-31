from datetime import datetime
from src.config.firebase import get_db


class FirestoreService:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = get_db()

    def _collection(self):
        if self.db is None:
            raise Exception("Firebase no está configurado correctamente.")
        return self.db.collection(self.collection_name)

    def get_all(self):
        docs = self._collection().stream()
        data = []

        for doc in docs:
            item = doc.to_dict()
            item["id"] = doc.id
            data.append(item)

        return data

    def get_by_id(self, document_id):
        doc = self._collection().document(document_id).get()

        if not doc.exists:
            return None

        item = doc.to_dict()
        item["id"] = doc.id
        return item

    def create(self, data):
        data["created_at"] = datetime.utcnow().isoformat()
        data["updated_at"] = datetime.utcnow().isoformat()

        doc_ref = self._collection().document()
        doc_ref.set(data)

        data["id"] = doc_ref.id
        return data

    def update(self, document_id, data):
        doc_ref = self._collection().document(document_id)
        doc = doc_ref.get()

        if not doc.exists:
            return None

        data["updated_at"] = datetime.utcnow().isoformat()
        doc_ref.update(data)

        updated_doc = doc_ref.get().to_dict()
        updated_doc["id"] = document_id
        return updated_doc

    def delete(self, document_id):
        doc_ref = self._collection().document(document_id)
        doc = doc_ref.get()

        if not doc.exists:
            return False

        doc_ref.delete()
        return True   
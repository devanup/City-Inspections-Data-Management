# This file contains a class for performing various operations on a MongoDB database collection.
from bson import ObjectId
class DBOperations:
    def __init__(self, db):
        self.collection = db.project_1_collections
    
        # INSERT document
    def insert_document(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def insert_documents(self, documents):
        result = self.collection.insert_many(documents)
        return result.inserted_ids

    # DELETE document
    def delete_document(self, document_id):
        result = self.collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0

    # DELETE all documents
    def delete_all_documents(self):
        result = self.collection.delete_many({})
        return result.deleted_count

    # FIND document
    def find_document(self, query):
        result = self.collection.find_one(query)
        return result

    # UPDATE document
    def update_document(self, document_id, update_data):
        result = self.collection.update_one(
            {"_id": document_id},
            {"$set": update_data}
        )
        return result.modified_count > 0

    # COUNT documents
    def count_documents(self, query=None):
        if query is None:
            return self.collection.count_documents({})
        else:
            return self.collection.count_documents(query)

    # CLOSE connection
    def close_connection(self):
        self.collection.database.client.close()

# This file contains a class for performing various operations on a MongoDB database collection.
class DBOperations:
    def __init__(self, db):
        self.collection = db.project_1_collection
    
    # INSERT document
    def insert_document(self, data):
        pass

    def insert_documents(self, documents):
        pass

    # DELETE document
    def delete_document(self, document_id):
        pass
    
    # DELETE all documents
    def delete_all_documents(self):
        pass

    # FIND document
    def find_document(self, query):
        pass

    # UPDATE document
    def update_document(self, document_id, update_data):
        pass

    # COUNT documents
    def count_documents(self, query=None):
        pass
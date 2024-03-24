# This file contains a class for performing various operations on a MongoDB database collection.

import pprint
from bson import ObjectId
class DBOperations:
    def __init__(self, db):
        self.collection = db.project_1_collections
    
        # INSERT document
    def insert_document(self, data):
        result = self.collection.insert_one(data).inserted_id
        print("Document inserted successfully with ID",result.inserted_id)
        return result.inserted_id

    def insert_documents(self, documents):
        result = self.collection.insert_many(documents)
        print("Documents inserted successfully.")
        return result.inserted_ids

    # DELETE document
    def delete_document(self, document_id):
        result = self.collection.delete_one({"_id": ObjectId(document_id)})
        if result.deleted_count == 1:
            print("Document deleted successfully.")
        else:
            print("Document not found or could not be deleted.")
        return result.deleted_count > 0

    # DELETE all documents
    def delete_all_documents(self):
        result = self.collection.delete_many({})

        if result.deleted_count == 0:
            print("No documents to delete.")
        else:
            print(f"{result.deleted_count} documents deleted successfully.")

    # FIND document
    def find_document(self, query):
        try:
            result_count = self.collection.count_documents(query)
            
            if result_count == 0:
                # print("No documents found matching the query.")
                return []  # Return an empty list if no documents found
            else:
                result = self.collection.find(query)
                return list(result)  # Convert cursor to a list of documents
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list in case of an error  

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

        if result.modified_count == 1:
            print("Document updated successfully.")
        else:
            print("Document not found or could not be updated.")

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
        print("Connection closed.")

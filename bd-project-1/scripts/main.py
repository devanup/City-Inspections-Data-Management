import json
from db_connection import DBConnection
from db_operations import DBOperations
from data_processor import DataProcessor

def main():
    # Create an instance of the DBConnection class
    db_connection = DBConnection()
    # Create an instance of the DBOperations class
    db_operations = DBOperations(db_connection.db)

    # Load JSON data from a file
    inspections_data = DataProcessor.load_json_data("../data/test.json")

    # Initialize database operations

    # Perform data operations
    # Insert documents into the collection
    
    # Loop through each data point and insert into the collection
    for data_point in inspections_data:
    # Insert each document individually
        inserted_id = db_operations.insert_document(data_point)
    # Print the counts for each year
    DataProcessor.count_inspections_by_year(inspections_data)

    
    # Close the database connection
    db_operations.close_connection()
    
if __name__ == "__main__":
    main()

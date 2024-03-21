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
    inspections_data = DataProcessor.load_json_data("../data/city_inspections.json")
    # Print first record
    print(inspections_data[0])
    
    # Initialize database operations

    # Load JSON data from file
    
    # Perform data operations

if __name__ == "__main__":
    main()

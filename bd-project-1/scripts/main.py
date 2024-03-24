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


    # Insert documents into the collection
    for data_point in inspections_data:
        inserted_id = db_operations.insert_document(data_point)
        
    # Print the counts for each year
    DataProcessor.count_inspections_by_year(inspections_data)

    # Ask the user for a business name
    business_name = input("Enter the name of the business: ").upper()

    # # Search for the business violation
    DataProcessor.find_business_violation(business_name, inspections_data)
    
    #print violations for Brooklyn, Bronx and difference
    DataProcessor.count_and_print_borough_violations(inspections_data)
    
    #Find 5 random businesses
    zip_code = int(input("Enter a zip code to find 5 businesses in the area: "))
    DataProcessor.search_businesses_by_zip(zip_code, inspections_data)
    
    # Close the database connection
    db_operations.close_connection()
    
if __name__ == "__main__":
    main()

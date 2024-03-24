from db_connection import DBConnection
from db_operations import DBOperations
from data_processor import DataProcessor

def main():
    # Create an instance of the DBConnection class
    db_connection = DBConnection()

    # Create an instance of the DBOperations class
    db_operations = DBOperations(db_connection.db)

    # Delete all documents in the collection
    # db_operations.delete_all_documents()

    # Load JSON data from a file
    inspections_data = DataProcessor.load_json_data("../data/city_inspections.json")

    # Q1: Insert documents into the collection
    # db_operations.insert_documents(inspections_data)
        
    # Q2: Count documents with date containing the year 2015 & 2016
    DataProcessor.count_inspections_by_year(inspections_data)

    # Q3: Ask the user for a business name
    business_name = input("Enter the name of the business: ").upper()
    # Q3: Search for the business violation
    DataProcessor.find_business_violation(business_name, inspections_data)

    #Q4:
    # Count violations in Brooklyn
    count_brooklyn = DataProcessor.count_violations_by_borough(db_operations, "BROOKLYN")
    # Count violations in Bronx
    count_bronx = DataProcessor.count_violations_by_borough(db_operations, "BRONX")
    # Print total violations in Brooklyn and Bronx
    print(f"Total violations in Brooklyn: {count_brooklyn}")
    print(f"Total violations in Bronx: {count_bronx}")
    # Calculate the difference in counts between Brooklyn and Bronx
    difference = abs(count_brooklyn - count_bronx)
    print(f"Difference in counts between Brooklyn and Bronx: {difference}")
    
    # Q5: Find businesses in a zip code
    DataProcessor.find_businesses_in_zip_code(db_operations)
    
    # Close the database connection
    db_operations.close_connection()
    
if __name__ == "__main__":
    main()

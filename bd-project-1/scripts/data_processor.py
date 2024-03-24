import json
import os
import random
class DataProcessor:
    @staticmethod
    def load_json_data(file_name):
        file_path = os.path.join(os.path.dirname(__file__), file_name) # Constructing the absolute file path
        
        data = [] # Initializing an empty list to store the JSON data

        with open(file_path, 'r') as file:
            for line in file:
                try:
                    json_data = json.loads(line)
                    if "_id" in json_data and isinstance(json_data["_id"], dict) and "$oid" in json_data["_id"]:
                        # Ignore entries with "_id" as "$oid"
                        del json_data["_id"]
                    data.append(json_data) # Appending data without "_id" as "$oid" to the list
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue
        
        return data # Returning the list of JSON data without "_id" as "$oid"
    
    @staticmethod
    def count_inspections_by_year(inspections_data):
        year_counts = {}  # Dictionary to store counts for each year dynamically

        for inspection in inspections_data:
            if "date" in inspection:
                # Extract the year from the date string
                year = int(inspection["date"].split()[-1])
                # Increment count for the respective year
                year_counts[year] = year_counts.get(year, 0) + 1

        # Print the year_counts and count for each year
        for year, count in year_counts.items():
            print(f"Number of Inspections in {year}: {count}")

        print("Year Counts:", year_counts)
        print()
        
    @staticmethod
    def find_business_violation(business_name, inspections_data):
        result = None
        #Search for business_name
        for inspection in inspections_data:
            if "business_name" in inspection and inspection["business_name"] == business_name:
                result = inspection["result"]
                break

        # Print the result or "Business Not found"
        if result is not None:
            print(f"Result for '{business_name}': {result} \n")
        else:
            print("Business Not found. \n")

    @staticmethod
    def count_violations_by_borough(db_operations, borough):
        # Construct query to match documents with the given borough
        query = {"address.city": borough}
        
        # Find documents matching the query
        documents = db_operations.find_document(query)
        
        # Initialize variables to count violations
        violation_count = 0

        # Initialize lists to store businesses
        businesses = []

        # Iterate through documents to count violations and collect business information
        for doc in documents:
            if doc["result"] == "Violation Issued":
                violation_count += 1
            
            # Append business information to the list
            businesses.append({
                "business_name": doc.get("business_name", ""),
                "address": doc.get("address", {})
            })

        
        return violation_count

    @staticmethod
    def print_businesses_by_borough(db_operations, borough, limit=5):
        # Construct query to match documents with the given borough
        query = {"address.city": borough}
        
        # Find documents matching the query
        documents = db_operations.find_document(query)
        
        # Print the names and addresses of the first five businesses in the borough
        print(f"\nFirst {limit} businesses located in {borough}:")
        for i, business in enumerate(documents[:limit]):
            print(f"{i+1}. Name: {business['business_name']}, Address: {business['address']['number']} {business['address']['street']}, {borough}, {business['address']['zip']}")

    @staticmethod
    def print_random_businesses(documents):
        # Randomly select five businesses from the list
        random_businesses = random.sample(documents, min(5, len(documents)))
        
        # Print the names of the randomly selected businesses
        print("\nRandomly selected businesses:")
        for i, business in enumerate(random_businesses, start=1):
            print(f"{i}. {business['business_name']}")

    @staticmethod
    def businesses_in_zip_code(db_operations, zip_code):
        # Construct query to match documents with the given zip code
        query = {"address.zip": zip_code}
        
        # Find documents matching the query
        documents = db_operations.find_document(query)
        
        # Count the total number of businesses in the zip code
        total_businesses = len(documents)
        
        return documents, total_businesses

    @staticmethod
    def find_businesses_in_zip_code(db_operations):
        # Prompt the user to input a zip code
        zip_code = input("\nEnter a zip code: ")
        
        # Check if the zip code is valid
        if not zip_code.isdigit():
            print("Invalid zip code. Please enter a numeric zip code.")
            return
        
        # Convert zip code to integer
        zip_code = int(zip_code)
        
        # Get the businesses in the specified zip code
        documents, total_businesses = DataProcessor.businesses_in_zip_code(db_operations, zip_code)
        
        # Check if any businesses were found in the zip code
        if total_businesses == 0:
            print("Zip code not found.")
            return

        # Print the total number of businesses in the zip code
        print(f"Total number of businesses in zip code {zip_code}: {total_businesses}")
        
        # Print the names of randomly selected businesses
        DataProcessor.print_random_businesses(documents)
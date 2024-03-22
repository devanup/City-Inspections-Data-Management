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
    def count_and_print_borough_violations(inspections_data):
        count_brooklyn = 0
        count_bronx = 0
        brooklyn_businesses = []
        bronx_businesses = []

        for inspection in inspections_data:
            if "address" in inspection:
                address = inspection["address"]
                city = address.get("city", "").upper()

                if city == "BROOKLYN":
                    count_brooklyn += 1
                    if len(brooklyn_businesses) < 5:
                        brooklyn_businesses.append({
                            "business_name": inspection.get("business_name", ""),
                            "address": address
                        })
                elif city == "BRONX":
                    count_bronx += 1
                    if len(bronx_businesses) < 5:
                        bronx_businesses.append({
                            "business_name": inspection.get("business_name", ""),
                            "address": address
                        })

        print("Business Violations in Brooklyn:")
        for business in brooklyn_businesses:
            print(f"Name: {business['business_name']}")
            print(f"Address: {business['address']} \n")

        print("Business Violations in Bronx:")
        for business in bronx_businesses:
            print(f"Name: {business['business_name']}")
            print(f"Address: {business['address']} \n")


        print("Total Violations in Brooklyn:", count_brooklyn)
        print("Total Violations in Bronx:", count_bronx)

        difference = abs(count_brooklyn - count_bronx)
        print("Difference in Violations Count:", difference)
        
    
    @staticmethod
    def search_businesses_by_zip(zip_code, inspections_data):
        matching_businesses = []
        #Search for Zip-code
        for inspection in inspections_data:
            address = inspection.get("address", {})
            if "zip" in address and address["zip"] == zip_code:
                matching_businesses.append(inspection["business_name"])
        
        if matching_businesses:
            print(f"Total number of businesses in zip code {zip_code}: {len(matching_businesses)}")

            # Randomly select 5 or less businesses
            min_businesses = min(5, len(matching_businesses))
            selected_businesses = random.sample(matching_businesses, min_businesses)

            print("Randomly selected businesses:")
            for business in selected_businesses:
                print(business)
        else:
            print("Zip-code Not found.")
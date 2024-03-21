import json
import os

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

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

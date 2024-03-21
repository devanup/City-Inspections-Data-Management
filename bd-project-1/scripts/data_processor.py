# This file is a class that contains a method to load JSON data from a file.
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
                    data.append(json.loads(line)) # Parsing the JSON data and appending it to the list
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue
        
        return data # Returning the list of JSON data

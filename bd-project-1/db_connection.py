# This file contains a class for establishing a connection to the MongoDB database.
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os 

class DBConnection:
    def __init__(self):
        load_dotenv(find_dotenv()) # Load environment variables from .env file
        password = os.environ.get("MONGO_PWD") # Get the password from environment variables
        connection_string = f"mongodb+srv://anupthedev:{password}@bigdata-project1.3h2wcf2.mongodb.net/" # Get MongoDB connection string from environment variables
        self.client = MongoClient(connection_string) # Connect to MongoDB
        self.db = self.client["Project01"] # Access the database

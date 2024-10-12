from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://abubilal:Ecw3uS8dgWBZqkaV@abu.5drgr.mongodb.net/?retryWrites=true&w=majority&appName=abu"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]
rec_collection = db["records"]

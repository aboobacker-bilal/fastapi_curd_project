from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from const import BASE_URLS

uri = BASE_URLS

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]
rec_collection = db["records"]

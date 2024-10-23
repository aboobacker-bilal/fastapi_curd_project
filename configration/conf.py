from pydantic.v1 import BaseSettings
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Settings(BaseSettings):
    MONGO_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

client = MongoClient(settings.MONGO_URL, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]
rec_collection = db["records"]

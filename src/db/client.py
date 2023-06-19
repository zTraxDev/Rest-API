from pymongo import MongoClient
from src.models.Product_Model import Product

class DataBase:
    def __init__(self, URI: str, database: str, collection: str):
        self.client = MongoClient(database)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def show_all_item(self):
        return self.collection.find()
    
    def show_item(self, id):
        return self.collection.find_one({"_id": id})
    
    def create_item(self, item: Product):
        return self.collection.insert_one(item).inserted_id
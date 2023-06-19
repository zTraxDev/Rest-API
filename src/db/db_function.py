from src.db.client import products_collection, users_collection


def inser_item(item):
    return products_collection.insert_one(dict(item)).inserted_id 

def search_item(item):
    return products_collection.find_one({"_id": item})

def delete_item(item):
    return products_collection.find_one_and_delete({"_id": item})


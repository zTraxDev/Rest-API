from fastapi import APIRouter, HTTPException, status
from src.db.client import products_collection, users_collection
from bson import ObjectId
from src.models.Product_Model import Product
from src.middleware.functions import productEntity, show_all_products
from src.db.db_function import *

router = APIRouter(prefix="/products")

@router.get("/")
async def view_products():
    return show_all_products(products_collection.find())


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_item(product: Product):
   new_item = dict(product)
   name = new_item.get('name')
   query = products_collection.find_one({"name": name})
   
   if query is not None:
       raise HTTPException(status.HTTP_404_NOT_FOUND, "User is Create")
   
   id = products_collection.insert_one(new_item).inserted_id
   query = products_collection.find_one({"_id": id})
   return productEntity(query)
products_collection.aggregate


@router.delete("/{id}")
async def delete_item(id: str):
    query = products_collection.find_one({"_id": ObjectId(id)})
    if query is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Producto No encontrado")
    products_collection.find_one_and_delete({"_id": ObjectId(id)})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Delete Successful")
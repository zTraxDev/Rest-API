import pymongo

try:
    client = pymongo.MongoClient('localhost', 27017)
    db = client['my_database']
    users_collection = db['users']
    products_collection = db['products']
    print(f"Database Load ✔️  | PyMongo: {pymongo.__version__}")
except Exception as e:
     print(f"Error al Conectar {e}")
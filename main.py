from fastapi import FastAPI
from src.routes.products import router

app = FastAPI(debug=True)
app.include_router(router)

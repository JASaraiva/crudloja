from fastapi import FastAPI
from app.routers import category
from app.routers import product
from app.routers import user

from . import config

app = FastAPI()


@app.get("/")
def home() -> dict:
    return {
        "message": "API Loja"
    }

app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
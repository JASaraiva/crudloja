from fastapi import FastAPI
from app.routers import products, categories, users
from app.database import Base, engine


app = FastAPI()

@app.get("/")
def home() -> dict:
    return {
        "message": "API Loja"
    }

app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)
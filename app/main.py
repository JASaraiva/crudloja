from fastapi import FastAPI
from app.routers import category, product, user
from app.database import Base, engine


app = FastAPI()

@app.get("/")
def home() -> dict:
    return {
        "message": "API Loja"
    }

app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
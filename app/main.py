from fastapi import FastAPI

from app.routers import (
    category, 
    product, 
    order, 
    role, 
    payment, 
    payment_method, 
    advertisement, 
    rating, 
    comment, 
    user, 
    auth
)


app = FastAPI()


@app.get("/")
def home() -> dict:
    return {
        "message": "API Loja"
    }

app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)
app.include_router(role.router)
app.include_router(payment.router)
app.include_router(payment_method.router)
app.include_router(advertisement.router)
app.include_router(rating.router)
app.include_router(comment.router)
app.include_router(auth.router)
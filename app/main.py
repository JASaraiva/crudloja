from fastapi import FastAPI
from app.routers import category
from app.routers import product
from app.routers import order
from app.routers import role
from app.routers import payment
from app.routers import payment_method
from app.routers import advertisement
from app.routers import rating
from app.routers import comment
from app.routers import user


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
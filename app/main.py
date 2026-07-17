from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.exceptions.business import BusinessException
from app.exceptions.repository import RepositoryIntegrityException
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
    auth,
)

app = FastAPI()


@app.get("/")
def home() -> dict:
    return {"message": "API Loja"}


app.include_router(advertisement.router)
app.include_router(auth.router)
app.include_router(category.router)
app.include_router(comment.router)
app.include_router(order.router)
app.include_router(payment.router)
app.include_router(payment_method.router)
app.include_router(product.router)
app.include_router(rating.router)
app.include_router(role.router)
app.include_router(user.router)


@app.exception_handler(BusinessException)
async def business_exception_handler(request, exc: BusinessException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


@app.exception_handler(RepositoryIntegrityException)
async def integrity_exception_handler(request, exc: RepositoryIntegrityException):
    return JSONResponse(
        status_code=409,
        content={"detail": exc.message},
    )

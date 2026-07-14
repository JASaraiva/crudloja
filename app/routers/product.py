from fastapi import APIRouter, status, Depends

from app.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.services import ProductService
from app.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def list(service: ProductService = Depends(get_product_service)) -> list[ProductResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: ProductService = Depends(get_product_service)) -> ProductResponse:
    return service.get(id)

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(product: ProductCreate, service: ProductService = Depends(get_product_service)) -> ProductResponse:
    return service.create(product)

@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update(id: int, product: ProductUpdate, service: ProductService = Depends(get_product_service)) -> ProductResponse:
    return service.update(id, product)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: ProductService = Depends(get_product_service)) -> None:
    service.delete(id)

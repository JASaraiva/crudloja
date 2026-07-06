from fastapi import APIRouter, status, Depends
from app import schemas
from app.services import ProductService
from app.denpendencies import get_product_service

router = APIRouter(prefix="/products", tags=["produtos"])

@router.get("/")
def list_products(service: ProductService = Depends(get_product_service)) -> list[schemas.ProductResponse]:
    return service.list_products()

@router.get("/{id}")
def get_product(id: int, service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.get_product(id)

@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.create_product(product)

@router.put("/{id}", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def update_product(id: int, product: schemas.ProductUpdate, service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.update_product(id, product)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, service: ProductService = Depends(get_product_service)) -> None:
    service.delete_product(id)

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.services import ProductService
from app.database import get_db
from app.dependency import get_product_service

router = APIRouter(prefix="/products", tags=["produtos"])

@router.get("/")
def list_products(db: Session = Depends(get_db), service: ProductService = Depends(get_product_service)) -> list[schemas.ProductResponse]:
    return service.list_products(db)

@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db), service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.get_product(db, id)


@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.create_product(db, product)


@router.put("/{id}", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db), service: ProductService = Depends(get_product_service)) -> schemas.ProductResponse:
    return service.update_product(db, id, product)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db), service: ProductService = Depends(get_product_service)) -> None:
    service.delete_product(db, id)
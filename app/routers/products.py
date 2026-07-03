from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import ProductCreate, ProductResponse, ProductUpdate
from app import crud
from app.database import get_db

router = APIRouter(prefix="/products", tags=["produtos"])
session = Depends(get_db)

@router.get("/")
def list_products(db: Session = session) -> list[ProductResponse]:
    return crud.list_products(db)

@router.get("/{id}")
def get_product(id: int, db: Session = session) -> ProductResponse:
    return crud.get_product(db, id)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = session) -> ProductResponse:
    return crud.create_product(db, product)


@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(id: int, product: ProductUpdate, db: Session = session) -> ProductResponse:
    return crud.update_product(db, id, product)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id: int, db: Session = session):
    return crud.delete_product(db, id)
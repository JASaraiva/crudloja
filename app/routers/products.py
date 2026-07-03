from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter(prefix="/products", tags=["produtos"])
session = Depends(get_db)

@router.get("/")
def list_products(db: Session = session) -> list[schemas.ProductResponse]:
    return services.list_products(db)

@router.get("/{id}")
def get_product(id: int, db: Session = session) -> schemas.ProductResponse:
    return services.get_product(db, id)


@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = session) -> schemas.ProductResponse:
    return services.create_product(db, product)


@router.put("/{id}", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = session) -> schemas.ProductResponse:
    return services.update_product(db, id, product)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id: int, db: Session = session):
    return services.delete_product(db, id)
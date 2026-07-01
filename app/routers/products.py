from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import ProductCreate, ProductResponse
from app.crud import crud
from app.database import get_db

router = APIRouter(prefix="/products", tags=["produtos"])

@router.get("/")
def list_products() -> list[dict]:
    return  [
    {
        "id": 1,
        "name": "Notebook"
    },
    {
        "id": 2,
        "name": "Mouse"
    }
]


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> ProductResponse:
    return crud.create_product(db, product)
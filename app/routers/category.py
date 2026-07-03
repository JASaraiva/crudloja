from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.repositories import category
from app.database import get_db

router = APIRouter(prefix = "/categories",
                   tags=["categorias"])

session = Depends(get_db)

@router.get("/")
def list_categories(db: Session = session) -> list[CategoryResponse]:
    return category.list_categories(db)

@router.get("/{id}")
def get_category(id: int, db: Session = session) -> CategoryResponse:
    return category.get_category(db, id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = session) -> CategoryResponse:
    return category.create_category(db, category)


@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category(id: int, category: CategoryUpdate, db: Session = session) -> CategoryResponse:
    return category.update_category(db, id, category)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_category(id: int, db: Session = session):
    return category.delete_category(db, id)
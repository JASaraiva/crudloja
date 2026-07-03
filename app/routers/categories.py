from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app import repository
from app.database import get_db

router = APIRouter(prefix = "/categories",
                   tags=["categorias"])

session = Depends(get_db)

@router.get("/")
def list_categories(db: Session = session) -> list[CategoryResponse]:
    return repository.list_categories(db)

@router.get("/{id}")
def get_category(id: int, db: Session = session) -> CategoryResponse:
    return repository.get_category(db, id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = session) -> CategoryResponse:
    return repository.create_category(db, category)


@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category(id: int, category: CategoryUpdate, db: Session = session) -> CategoryResponse:
    return repository.update_category(db, id, category)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_category(id: int, db: Session = session):
    return repository.delete_category(db, id)
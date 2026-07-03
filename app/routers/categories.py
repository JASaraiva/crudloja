from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app import crud
from app.database import get_db

router = APIRouter(prefix = "/categories",
                   tags=["categorias"])

session = Depends(get_db)

@router.get("/")
def list_categories(db: Session = session) -> list[CategoryResponse]:
    return crud.list_categories(db)

@router.get("/{id}")
def get_category(id: int, db: Session = session) -> CategoryResponse:
    return crud.get_category(db, id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = session) -> CategoryResponse:
    return crud.create_category(db, category)


@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category(id: int, category: CategoryUpdate, db: Session = session) -> CategoryResponse:
    return crud.update_category(db, id, category)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_category(id: int, db: Session = session):
    return crud.delete_category(db, id)
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import CategoryService
from app.database import get_db
from app.denpendencies import get_category_service

router = APIRouter(prefix="/categories", tags=["categorias"])

@router.get("/")
def list_categories(db: Session = Depends(get_db), service: CategoryService = Depends(get_category_service)) -> list[CategoryResponse]:
    return service.list_categories(db)

@router.get("/{id}")
def get_category(id: int, db: Session = Depends(get_db), service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.get_category(db, id)

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db), service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.create_category(db, category_data)

@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category(id: int, category_data: CategoryUpdate, db: Session = Depends(get_db), service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.update_category(db, id, category_data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int, db: Session = Depends(get_db), service: CategoryService = Depends(get_category_service)) -> None:
    service.delete_category(db, id)

from fastapi import APIRouter, status, Depends
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import CategoryService
from app.denpendencies import get_category_service

router = APIRouter(prefix="/categories", tags=["categorias"])

@router.get("/")
def list_categories(service: CategoryService = Depends(get_category_service)) -> list[CategoryResponse]:
    return service.list_categories()

@router.get("/{id}")
def get_category(id: int, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.get_category(id)

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.create_category(category_data)

@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category(id: int, category_data: CategoryUpdate, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.update_category(id, category_data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int, service: CategoryService = Depends(get_category_service)) -> None:
    service.delete_category(id)

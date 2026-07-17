from fastapi import APIRouter, Depends, status

from app.dependencies import get_current_user, get_category_service
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
def list(service: CategoryService = Depends(get_category_service)) -> list[CategoryResponse]:
    return service.list()


@router.get("/{id}")
def get(id: int, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.get(id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create(category: CategoryCreate, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.create(category)


@router.put("/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update(id: int, category: CategoryUpdate, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return service.update(id, category)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: CategoryService = Depends(get_category_service)) -> None:
    service.delete(id)

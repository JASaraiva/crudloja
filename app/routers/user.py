from fastapi import APIRouter, status, Depends

from app.schemas import UserCreate, UserUpdate, UserResponse
from app.services import UserService
from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list(service: UserService = Depends(get_user_service)) -> list[UserResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.get(id)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.create(user)

@router.put("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update(id: int, user: UserUpdate, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.update(id, user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: UserService = Depends(get_user_service)) -> None:
    service.delete(id)

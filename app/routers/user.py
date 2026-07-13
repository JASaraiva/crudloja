from fastapi import APIRouter, status, Depends
from app.schemas import UserCreate, UserUpdate, UserResponse
from app.services import UserService
from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users(service: UserService = Depends(get_user_service)) -> list[UserResponse]:
    return service.list_users()

@router.get("/{id}")
def get_user(id: int, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.get_user(id)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.create_user(user)

@router.put("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(id: int, user: UserUpdate, service: UserService = Depends(get_user_service)) -> UserResponse:
    return service.update_user(id, user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, service: UserService = Depends(get_user_service)) -> None:
    service.delete_user(id)

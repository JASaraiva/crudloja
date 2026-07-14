from fastapi import APIRouter, status, Depends

from app.schemas import RoleCreate, RoleUpdate, RoleResponse
from app.services import RoleService
from app.dependencies import get_role_service

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/")
def list(service: RoleService = Depends(get_role_service)) -> list[RoleResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.get(id)

@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create(role: RoleCreate, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.create(role)

@router.put("/{id}", response_model=RoleResponse, status_code=status.HTTP_200_OK)
def update(id: int, role: RoleUpdate, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.update(id, role)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: RoleService = Depends(get_role_service)) -> None:
    service.delete(id)

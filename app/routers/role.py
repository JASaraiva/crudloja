from fastapi import APIRouter, status, Depends
from app.schemas import RoleCreate, RoleUpdate, RoleResponse
from app.services import RoleService
from app.dependencies import get_role_service

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/")
def list_roles(service: RoleService = Depends(get_role_service)) -> list[RoleResponse]:
    return service.list_roles()

@router.get("/{id}")
def get_role(id: int, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.get_role(id)

@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(role: RoleCreate, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.create_role(role)

@router.put("/{id}", response_model=RoleResponse, status_code=status.HTTP_200_OK)
def update_role(id: int, role: RoleUpdate, service: RoleService = Depends(get_role_service)) -> RoleResponse:
    return service.update_role(id, role)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(id: int, service: RoleService = Depends(get_role_service)) -> None:
    service.delete_role(id)

from fastapi import APIRouter, Depends

from app.dependencies import get_auth_service, get_current_user
from app.schemas import AuthLogin, TokenSchema
from app.services import AuthService

router = APIRouter(prefix="", tags=["auth"])


@router.post("/login", response_model=TokenSchema)
def login(credentials: AuthLogin, service: AuthService = Depends(get_auth_service)) -> TokenSchema:
    return service.login(credentials)


@router.get("/me")
def me(current_user=Depends(get_current_user)) -> dict:
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email}

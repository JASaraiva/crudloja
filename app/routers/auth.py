from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_auth_service, get_current_user
from app.schemas import AuthLogin, TokenSchema
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenSchema)
def login(credentials: AuthLogin, service: AuthService = Depends(get_auth_service)) -> TokenSchema:
    return service.login(credentials)


@router.get("/me")
def me(service: AuthService = Depends(get_current_user)) -> dict:
    return service.get_current_user_data()

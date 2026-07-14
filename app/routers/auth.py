from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_auth_service, get_current_user
from app.exceptions import UnauthorizedException
from app.models import User
from app.schemas import AuthLogin, TokenSchema
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenSchema)
def login(credentials: AuthLogin, service: AuthService = Depends(get_auth_service)) -> TokenSchema:
    try:
        return service.login(credentials)
    except UnauthorizedException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@router.get("/me")
def me(current_user: User = Depends(get_current_user)) -> dict:
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email}

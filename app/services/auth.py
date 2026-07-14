from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.repositories import UserRepository
from app.models import User


class AuthService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    
    def authenticate_user(self, username: str, password: str) -> User:
        user = self.user_repo.get_by_username(username)
        
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário ou senha incorretos"
                header={"WWW-Authenticate": "Bearer"},
            )
        
        return user
    
    def generate_token(self, username: str) -> str:
        return create_access_token(subject=username)
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.dependencies.sessions import get_db
from app.models import User
from app.repositories import UserRepository
from app.utils.auth import SECRET_KEY, ALGORITHM

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(token: str = Depends(_oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise _credentials_exception
    except JWTError:
        raise _credentials_exception

    user = UserRepository(db).get_by_email(email)
    if user is None:
        raise _credentials_exception

    return user

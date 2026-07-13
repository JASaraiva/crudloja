from sqlalchemy.orm import Session
from app.models import User
from app.repositories.base import BaseRepository
from app.schemas import UserCreate, UserUpdate


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):

    def __init__(self, db: Session):
        super().__init__(User, db)

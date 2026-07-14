from sqlalchemy.orm import Session
from app.models import User
from app.repositories.base import BaseRepository
from app.schemas import UserCreate, UserUpdate


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):

    def __init__(self, db: Session):
        super().__init__(User, db)

    def create(self, user: UserCreate) -> User:
        db_user = User(**user.model_dump)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
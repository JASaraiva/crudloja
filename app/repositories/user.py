from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User
from app.schemas import UserCreate, UserUpdate


class UserRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def get_user(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_users(self) -> list[User]:
        stmt = select(User)
        return self.db.execute(stmt).scalars().all()


    def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        user = self.get_user(user_id)

        for key, value in user_data.model_dump().items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user


    def delete_user(self, user_id: int) -> None:
        user = self.get_user(user_id)
        self.db.delete(user)
        self.db.commit()

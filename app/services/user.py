from app.repositories import UserRepository
from app.exceptions import (
    UserNotFoundException,
    UserHasRatingsException,
    UserHasCommentsException,
    UserHasPaymentsException,
)
from app.models import User
from app.schemas import UserCreate, UserUpdate
from app.utils import get_password_hash


class UserService():
    
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def get_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)

    def get(self, user_id: int) -> User:
        user = self.repository.get(user_id)

        if user is None:
            raise UserNotFoundException()
        
        return user
    

    
    def list(self) -> User:
        user = self.repository.list()
        return user
    

    def create(self, user_data: UserCreate) -> User:
        user_data.password = get_password_hash(user_data.password)
        return self.repository.create(user_data)

    def update(self, user_id: int, user_data: UserUpdate) -> User:
        if user_data.password is not None:
            user_data.password = get_password_hash(user_data.password)
        updated = self.repository.update(user_id, user_data)
        if updated is None:
            raise UserNotFoundException()
        return updated
    

    def delete(self, user_id: int) -> bool:
        user = self.get(user_id)

        if user.ratings:
            raise UserHasRatingsException()
        if user.comments:
            raise UserHasCommentsException()
        if user.payments:
            raise UserHasPaymentsException()

        self.repository.delete(user_id)
        return True

        
        

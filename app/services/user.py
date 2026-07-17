from app.repositories import UserRepository
from app.exceptions import (
    UserNotFoundException,
    UserHasRatingsException,
    UserHasCommentsException,
    UserHasPaymentsException,
)
from app.models import User
from app.schemas import UserCreate


class UserService():
    
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def get(self, user_id: int) -> User:
        user = self.repository.get(user_id)

        if user is None:
            raise UserNotFoundException(user_id)
        
        return user
    

    
    def list(self) -> User:
        user = self.repository.list()
        return user
    

    def create(self, user_data: UserCreate) -> User: 
        return self.repository.create(user_data)
    

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

        
        

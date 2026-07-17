from app.repositories import UserRepository
from app.exceptions import (
    UserNotFoundException,
    UserHasDependenciesException, 
    RepositoryIntegrityException
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

        try:
            self.repository.delete(user_id)
        except RepositoryIntegrityException:
            raise UserHasDependenciesException()

        return True

        
        

from app.repositories import UserRepository
from app.exceptions import UserNotFoundException
from app.models import User
from app.schemas import UserCreate


class UserService():
    
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def get_user(self, user_id: int) -> User:

        user = self.repository.get_user(user_id)

        if user is None:
            raise UserNotFoundException(user_id)
        
        return user
    

    
    def list_users(self) -> User:
        user = self.repository.list_users()
        return user
    

    def create_user(self, user_data: UserCreate) -> User: 
        return self.repository.create_user(user_data)
        

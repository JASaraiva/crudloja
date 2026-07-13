from app.repositories import RoleRepository
from app.exceptions import RoleNotFoundException
from app.models import Role
from app.schemas import RoleCreate


class RoleService():
    
    def __init__(self, repository: RoleRepository):
        self.repository = repository


    def get(self, role_id: int) -> Role:

        role = self.repository.get(role_id)

        if role is None:
            raise RoleNotFoundException(role_id)
        
        return role
    

    
    def list(self) -> Role:
        roles = self.repository.list()
        return roles
    

    def create(self, role_data: RoleCreate) -> Role: 
        return self.repository.create(role_data)
        

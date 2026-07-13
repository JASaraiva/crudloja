from app.repositories import RoleRepository
from app.exceptions import RoleNotFoundException
from app.models import Role
from app.schemas import RoleCreate


class RoleService():
    
    def __init__(self, repository: RoleRepository):
        self.repository = repository


    def get_role(self, role_id: int) -> Role:

        role = self.repository.get_role(role_id)

        if role is None:
            raise RoleNotFoundException(role_id)
        
        return role
    

    
    def list_roles(self) -> Role:
        roles = self.repository.list_roles()
        return roles
    

    def create_role(self, role_data: RoleCreate) -> Role: 
        return self.repository.create_role(role_data)
        

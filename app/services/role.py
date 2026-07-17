from app.repositories import RoleRepository
from app.exceptions import RoleNotFoundException
from app.models import Role
from app.schemas import RoleCreate, RoleUpdate


class RoleService():

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def get(self, role_id: int) -> Role:
        role = self.repository.get(role_id)
        if role is None:
            raise RoleNotFoundException()
        return role

    def list(self) -> list[Role]:
        return self.repository.list()

    def create(self, role_data: RoleCreate) -> Role:
        return self.repository.create(role_data)

    def update(self, role_id: int, role_data: RoleUpdate) -> Role:
        updated = self.repository.update(role_id, role_data)
        if updated is None:
            raise RoleNotFoundException()
        return updated

    def delete(self, role_id: int) -> None:
        self.get(role_id)
        self.repository.delete(role_id)

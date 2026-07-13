from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Role
from app.schemas import RoleCreate, RoleUpdate


class RoleRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_role(self, role: RoleCreate) -> Role:
        db_role = Role(**role.model_dump())
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role


    def get_role(self, role_id: int) -> Role | None:
        stmt = select(Role).where(Role.id == role_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_roles(self) -> list[Role]:
        stmt = select(Role)
        return self.db.execute(stmt).scalars().all()


    def update_role(self, role_id: int, role_data: RoleUpdate) -> Role:
        role = self.get_role(role_id)

        for key, value in role_data.model_dump().items():
            setattr(role, key, value)
        self.db.commit()
        self.db.refresh(role)
        return role


    def delete_role(self, role_id: int) -> None:
        role = self.get_role(role_id)
        self.db.delete(role)
        self.db.commit()

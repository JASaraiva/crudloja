from sqlalchemy.orm import Session

from app.models import Role
from app.repositories.base import BaseRepository
from app.schemas import RoleCreate, RoleUpdate


class RoleRepository(BaseRepository[Role, RoleCreate, RoleUpdate]):

    def __init__(self, db: Session):
        super().__init__(Role, db)

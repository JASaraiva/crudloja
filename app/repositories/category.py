from sqlalchemy.orm import Session
from app.models import Category
from app.repositories.base import BaseRepository
from app.schemas import CategoryCreate, CategoryUpdate


class CategoryRepository(BaseRepository[Category, CategoryCreate, CategoryUpdate]):

    def __init__(self, db: Session):
        super().__init__(Category, db)

from sqlalchemy.orm import Session
from app.models import Product
from app.repositories.base import BaseRepository
from app.schemas import ProductCreate, ProductUpdate


class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):

    def __init__(self, db: Session):
        super().__init__(Product, db)

from sqlalchemy.orm import Session
from app.models import Order
from app.repositories.base import BaseRepository
from app.schemas import OrderCreate, OrderUpdate


class OrderRepository(BaseRepository[Order, OrderCreate, OrderUpdate]):

    def __init__(self, db: Session):
        super().__init__(Order, db)

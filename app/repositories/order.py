from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Order
from app.schemas import OrderCreate, OrderUpdate


class OrderRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_order(self, order: OrderCreate) -> Order:
        db_order = Order(**order.model_dump())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order


    def get_order(self, order_id: int) -> Order | None:
        stmt = select(Order).where(Order.id == order_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_orders(self) -> list[Order]:
        stmt = select(Order)
        return self.db.execute(stmt).scalars().all()


    def update_order(self, order_id: int, order_data: OrderUpdate) -> Order:
        order = self.get_order(order_id)

        for key, value in order_data.model_dump().items():
            setattr(order, key, value)
        self.db.commit()
        self.db.refresh(order)
        return order


    def delete_order(self, order_id: int) -> None:
        order = self.get_order(order_id)
        self.db.delete(order)
        self.db.commit()

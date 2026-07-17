from app.repositories import OrderRepository
from app.exceptions import OrderNotFoundException
from app.models import Order
from app.schemas import OrderCreate, OrderUpdate


class OrderService():

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get(self, order_id: int) -> Order:
        order = self.repository.get(order_id)
        if order is None:
            raise OrderNotFoundException()
        return order

    def list(self) -> list[Order]:
        return self.repository.list()

    def create(self, order_data: OrderCreate) -> Order:
        return self.repository.create(order_data)

    def update(self, order_id: int, order_data: OrderUpdate) -> Order:
        updated = self.repository.update(order_id, order_data)
        if updated is None:
            raise OrderNotFoundException()
        return updated

    def delete(self, order_id: int) -> None:
        self.get(order_id)
        self.repository.delete(order_id)

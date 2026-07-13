from app.repositories import OrderRepository
from app.exceptions import OrderNotFoundException
from app.models import Order
from app.schemas import OrderCreate


class OrderService():
    
    def __init__(self, repository: OrderRepository):
        self.repository = repository


    def get(self, order_id: int) -> Order:

        order = self.repository.get(order_id)

        if order is None:
            raise OrderNotFoundException(order_id)
        
        return order
    

    
    def list(self) -> Order:
        orders = self.repository.list()
        return orders
    

    def create(self, order_data: OrderCreate) -> Order: 
        return self.repository.create(order_data)
        

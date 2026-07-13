from app.repositories import OrderRepository
from app.exceptions import OrderNotFoundException
from app.models import Order
from app.schemas import OrderCreate


class OrderService():
    
    def __init__(self, repository: OrderRepository):
        self.repository = repository


    def get_order(self, order_id: int) -> Order:

        order = self.repository.get_order(order_id)

        if order is None:
            raise OrderNotFoundException(order_id)
        
        return order
    

    
    def list_orders(self) -> Order:
        orders = self.repository.list_orders()
        return orders
    

    def create_order(self, order_data: OrderCreate) -> Order: 
        return self.repository.create_order(order_data)
        

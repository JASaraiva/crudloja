from app.repositories import PaymentMethodRepository
from app.exceptions import PaymentMethodNotFoundException
from app.models import PaymentMethod
from app.schemas import PaymentMethodCreate


class PaymentMethodService():
    
    def __init__(self, repository: PaymentMethodRepository):
        self.repository = repository


    def get_payment_method(self, payment_method_id: int) -> PaymentMethod:

        payment_method = self.repository.get_payment_method(payment_method_id)

        if payment_method is None:
            raise PaymentMethodNotFoundException(payment_method_id)
        
        return payment_method
    

    
    def list_payment_methods(self) -> PaymentMethod:
        payment_methods = self.repository.list_payment_methods()
        return payment_methods
    

    def create_payment_method(self, payment_method_data: PaymentMethodCreate) -> PaymentMethod: 
        return self.repository.create_payment_method(payment_method_data)
        

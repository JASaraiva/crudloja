from app.repositories import PaymentRepository
from app.exceptions import PaymentNotFoundException
from app.models import Payment
from app.schemas import PaymentCreate


class PaymentService():
    
    def __init__(self, repository: PaymentRepository):
        self.repository = repository


    def get_payment(self, payment_id: int) -> Payment:

        payment = self.repository.get_payment(payment_id)

        if payment is None:
            raise PaymentNotFoundException(payment_id)
        
        return payment
    

    
    def list_payments(self) -> Payment:
        payments = self.repository.list_payments()
        return payments
    

    def create_payment(self, payment_data: PaymentCreate) -> Payment: 
        return self.repository.create_payment(payment_data)
        

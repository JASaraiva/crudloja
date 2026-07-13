from app.repositories import PaymentRepository
from app.exceptions import PaymentNotFoundException
from app.models import Payment
from app.schemas import PaymentCreate


class PaymentService():
    
    def __init__(self, repository: PaymentRepository):
        self.repository = repository


    def get(self, payment_id: int) -> Payment:

        payment = self.repository.get(payment_id)

        if payment is None:
            raise PaymentNotFoundException(payment_id)
        
        return payment
    

    
    def list(self) -> Payment:
        payments = self.repository.list()
        return payments
    

    def create(self, payment_data: PaymentCreate) -> Payment: 
        return self.repository.create(payment_data)
        

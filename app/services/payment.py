from app.repositories import PaymentRepository
from app.exceptions import PaymentNotFoundException
from app.models import Payment
from app.schemas import PaymentCreate, PaymentUpdate


class PaymentService():

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def get(self, payment_id: int) -> Payment:
        payment = self.repository.get(payment_id)
        if payment is None:
            raise PaymentNotFoundException()
        return payment

    def list(self) -> list[Payment]:
        return self.repository.list()

    def create(self, payment_data: PaymentCreate) -> Payment:
        return self.repository.create(payment_data)

    def update(self, payment_id: int, payment_data: PaymentUpdate) -> Payment:
        updated = self.repository.update(payment_id, payment_data)
        if updated is None:
            raise PaymentNotFoundException()
        return updated

    def delete(self, payment_id: int) -> None:
        self.get(payment_id)
        self.repository.delete(payment_id)

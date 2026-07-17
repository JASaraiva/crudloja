from app.repositories import PaymentMethodRepository
from app.exceptions import PaymentMethodNotFoundException
from app.models import PaymentMethod
from app.schemas import PaymentMethodCreate, PaymentMethodUpdate


class PaymentMethodService():

    def __init__(self, repository: PaymentMethodRepository):
        self.repository = repository

    def get(self, payment_method_id: int) -> PaymentMethod:
        payment_method = self.repository.get(payment_method_id)
        if payment_method is None:
            raise PaymentMethodNotFoundException()
        return payment_method

    def list(self) -> list[PaymentMethod]:
        return self.repository.list()

    def create(self, payment_method_data: PaymentMethodCreate) -> PaymentMethod:
        return self.repository.create(payment_method_data)

    def update(self, payment_method_id: int, payment_method_data: PaymentMethodUpdate) -> PaymentMethod:
        updated = self.repository.update(payment_method_id, payment_method_data)
        if updated is None:
            raise PaymentMethodNotFoundException()
        return updated

    def delete(self, payment_method_id: int) -> None:
        self.get(payment_method_id)
        self.repository.delete(payment_method_id)

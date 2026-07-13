from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import PaymentMethod
from app.schemas import PaymentMethodCreate, PaymentMethodUpdate


class PaymentMethodRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_payment_method(self, payment_method: PaymentMethodCreate) -> PaymentMethod:
        db_payment_method = PaymentMethod(**payment_method.model_dump())
        self.db.add(db_payment_method)
        self.db.commit()
        self.db.refresh(db_payment_method)
        return db_payment_method


    def get_payment_method(self, payment_method_id: int) -> PaymentMethod | None:
        stmt = select(PaymentMethod).where(PaymentMethod.id == payment_method_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_payment_methods(self) -> list[PaymentMethod]:
        stmt = select(PaymentMethod)
        return self.db.execute(stmt).scalars().all()


    def update_payment_method(self, payment_method_id: int, payment_method_data: PaymentMethodUpdate) -> PaymentMethod:
        payment_method = self.get_payment_method(payment_method_id)

        for key, value in payment_method_data.model_dump().items():
            setattr(payment_method, key, value)
        self.db.commit()
        self.db.refresh(payment_method)
        return payment_method


    def delete_payment_method(self, payment_method_id: int) -> None:
        payment_method = self.get_payment_method(payment_method_id)
        self.db.delete(payment_method)
        self.db.commit()

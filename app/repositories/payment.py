from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Payment
from app.schemas import PaymentCreate, PaymentUpdate


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_payment(self, payment: PaymentCreate) -> Payment:
        db_payment = Payment(**payment.model_dump())
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)
        return db_payment


    def get_payment(self, payment_id: int) -> Payment | None:
        stmt = select(Payment).where(Payment.id == payment_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_payments(self) -> list[Payment]:
        stmt = select(Payment)
        return self.db.execute(stmt).scalars().all()


    def update_payment(self, payment_id: int, payment_data: PaymentUpdate) -> Payment:
        payment = self.get_payment(payment_id)

        for key, value in payment_data.model_dump().items():
            setattr(payment, key, value)
        self.db.commit()
        self.db.refresh(payment)
        return payment


    def delete_payment(self, payment_id: int) -> None:
        payment = self.get_payment(payment_id)
        self.db.delete(payment)
        self.db.commit()

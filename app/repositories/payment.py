from sqlalchemy.orm import Session
from app.models import Payment
from app.repositories.base import BaseRepository
from app.schemas import PaymentCreate, PaymentUpdate


class PaymentRepository(BaseRepository[Payment, PaymentCreate, PaymentUpdate]):

    def __init__(self, db: Session):
        super().__init__(Payment, db)

from sqlalchemy.orm import Session
from app.models import PaymentMethod
from app.repositories.base import BaseRepository
from app.schemas import PaymentMethodCreate, PaymentMethodUpdate


class PaymentMethodRepository(BaseRepository[PaymentMethod, PaymentMethodCreate, PaymentMethodUpdate]):

    def __init__(self, db: Session):
        super().__init__(PaymentMethod, db)

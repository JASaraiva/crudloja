from app.database import Base

from sqlalchemy import String, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
  

    payments: Mapped[list["Payment"]] = relationship(back_populates="payment_method")

    def __repr__(self) -> str:
        return f"PaymentMethod(id={self.id!r}, name={self.name!r})"

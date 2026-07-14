from app.database import Base

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("payment_methods.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    status: Mapped[int] = mapped_column(Numeric, default=0)

    user: Mapped["User"] = relationship(back_populates="payments")
    payment_method: Mapped["PaymentMethod"] = relationship(back_populates="payments")
    order: Mapped["Order"] = relationship(back_populates="payments")

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r})"

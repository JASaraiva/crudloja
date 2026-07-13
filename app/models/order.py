from sqlalchemy import Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    status: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    product: Mapped["Product"] = relationship(back_populates="orders")
    payments: Mapped[list["Payment"]] = relationship(back_populates="order")
  

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r})"

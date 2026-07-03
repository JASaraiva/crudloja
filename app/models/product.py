from sqlalchemy import String, Numeric, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base
from decimal import Decimal

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(Text)
    value: Mapped[Decimal] = mapped_column(Numeric(10,2))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    stock: Mapped[int] = mapped_column(default=0)

    category: Mapped["Category"] = relationship(back_populates="products")

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, value={self.value!r})"

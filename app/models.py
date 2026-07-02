from sqlalchemy import String, Numeric, DECIMAL, Text
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(Text)
    value: Mapped[DECIMAL] = mapped_column(Numeric(10,2))

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, value={self.value!r})"

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base


class Rating(Base):
    __tablename__ = "ratings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    value: Mapped[int] = mapped_column(Integer)

    product: Mapped["Product"] = relationship(back_populates="ratings")
    user: Mapped["User"] = relationship(back_populates="ratings")


    def __repr__(self) -> str:
        return f"Rating(id={self.id!r}, name={self.name!r})"

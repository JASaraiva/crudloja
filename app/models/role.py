from sqlalchemy import Text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
   
    def __repr__(self) -> str:
        return f"Rating(id={self.id!r}, name={self.name!r})"

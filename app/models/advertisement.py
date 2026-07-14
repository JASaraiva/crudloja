from sqlalchemy import String, Text
from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base

class Advertisement(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
  

    def __repr__(self) -> str:
        return f"Advertisement(id={self.id!r}, name={self.name!r}, description={self.description!r})"

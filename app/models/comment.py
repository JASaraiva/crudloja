from sqlalchemy import String, Text,  DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base
from datetime import datetime

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="comments")
  

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r})"

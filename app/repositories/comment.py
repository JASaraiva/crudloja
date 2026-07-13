from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Comment
from app.schemas import CommentCreate, CommentUpdate


class CommentRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_comment(self, comment: CommentCreate) -> Comment:
        db_comment = Comment(**comment.model_dump())
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment


    def get_comment(self, comment_id: int) -> Comment | None:
        stmt = select(Comment).where(Comment.id == comment_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_comments(self) -> list[Comment]:
        stmt = select(Comment)
        return self.db.execute(stmt).scalars().all()


    def update_comment(self, comment_id: int, comment_data: CommentUpdate) -> Comment:
        comment = self.get_comment(comment_id)

        for key, value in comment_data.model_dump().items():
            setattr(comment, key, value)
        self.db.commit()
        self.db.refresh(comment)
        return comment


    def delete_comment(self, comment_id: int) -> None:
        comment = self.get_comment(comment_id)
        self.db.delete(comment)
        self.db.commit()

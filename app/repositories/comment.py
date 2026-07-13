from sqlalchemy.orm import Session
from app.models import Comment
from app.repositories.base import BaseRepository
from app.schemas import CommentCreate, CommentUpdate


class CommentRepository(BaseRepository[Comment, CommentCreate, CommentUpdate]):

    def __init__(self, db: Session):
        super().__init__(Comment, db)

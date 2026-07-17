from app.repositories import CommentRepository
from app.exceptions import CommentNotFoundException
from app.models import Comment
from app.schemas import CommentCreate, CommentUpdate


class CommentService():

    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def get(self, comment_id: int) -> Comment:
        comment = self.repository.get(comment_id)
        if comment is None:
            raise CommentNotFoundException()
        return comment

    def list(self) -> list[Comment]:
        return self.repository.list()

    def create(self, comment_data: CommentCreate) -> Comment:
        return self.repository.create(comment_data)

    def update(self, comment_id: int, comment_data: CommentUpdate) -> Comment:
        updated = self.repository.update(comment_id, comment_data)
        if updated is None:
            raise CommentNotFoundException()
        return updated

    def delete(self, comment_id: int) -> None:
        self.get(comment_id)
        self.repository.delete(comment_id)

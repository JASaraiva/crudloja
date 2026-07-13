from app.repositories import CommentRepository
from app.exceptions import CommentNotFoundException
from app.models import Comment
from app.schemas import CommentCreate


class CommentService():
    
    def __init__(self, repository: CommentRepository):
        self.repository = repository


    def get(self, comment_id: int) -> Comment:

        comment = self.repository.get(comment_id)

        if comment is None:
            raise CommentNotFoundException(comment_id)
        
        return comment
    

    
    def list(self) -> Comment:
        comments = self.repository.list()
        return comments
    

    def create(self, comment_data: CommentCreate) -> Comment: 
        return self.repository.create(comment_data)
        

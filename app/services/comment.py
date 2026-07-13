from app.repositories import CommentRepository
from app.exceptions import CommentNotFoundException
from app.models import Comment
from app.schemas import CommentCreate


class CommentService():
    
    def __init__(self, repository: CommentRepository):
        self.repository = repository


    def get_comment(self, comment_id: int) -> Comment:

        comment = self.repository.get_comment(comment_id)

        if comment is None:
            raise CommentNotFoundException(comment_id)
        
        return comment
    

    
    def list_comments(self) -> Comment:
        comments = self.repository.list_comments()
        return comments
    

    def create_comment(self, comment_data: CommentCreate) -> Comment: 
        return self.repository.create_comment(comment_data)
        

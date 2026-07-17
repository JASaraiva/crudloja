from app.exceptions.base import AppException

class CommentNotFoundException(AppException):
    """Exception raised when a comment or comment to create a comment is not found."""
    pass
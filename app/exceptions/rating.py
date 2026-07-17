from app.exceptions.base import AppException

class RatingNotFoundException(AppException):
    """Exception raised when a rating or rating to create a rating is not found."""
    pass
from app.exceptions.base import AppException

class CategoryNotFoundException(AppException):
    """Exception raised when a category or category to create a category is not found."""
    pass
from app.exceptions.base import AppException

class ProductNotFoundException(AppException):
    """Exception raised when a product or category to create a product is not found."""
    pass
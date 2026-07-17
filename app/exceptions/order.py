from app.exceptions.base import AppException

class OrderNotFoundException(AppException):
    """Exception raised when a order or order to create a order is not found."""
    pass
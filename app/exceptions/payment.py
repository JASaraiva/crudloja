from app.exceptions.base import AppException

class PaymentNotFoundException(AppException):
    """Exception raised when a payment or payment to create a payment is not found."""
    pass
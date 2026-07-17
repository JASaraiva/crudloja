from app.exceptions.base import AppException

class PaymentMethodNotFoundException(AppException):
    """Exception raised when a payment method or payment method to create a payment method is not found."""
    pass
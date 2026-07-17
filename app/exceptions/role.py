from app.exceptions.base import AppException

class RoleNotFoundException(AppException):
    """Exception raised when a role or role to create a role is not found."""
    pass
from app.exceptions.base import AppException

        
class RepositoryIntegrityException(AppException):
    def __init__(self, message: str = "Operação violaria integridade referencial."):
        super().__init__(message)



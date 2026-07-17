from app.exceptions.business import BusinessException


class UnauthorizedException(BusinessException):
    status_code = 401

    def __init__(self):
        super().__init__("Usuário ou senha inválidos.")

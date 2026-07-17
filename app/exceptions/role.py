from app.exceptions.business import BusinessException


class RoleNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Perfil não encontrado.")

from app.exceptions.business import BusinessException


class UserNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Usuário não encontrado.")


class UserHasDependenciesException(BusinessException):
    status_code = 409

    def __init__(self):
        super().__init__("Não é possível remover o usuário porque existem registros associados.")


class UserHasRatingsException(BusinessException):
    status_code = 409

    def __init__(self):
        super().__init__("Não é possível remover o usuário porque ele possui avaliações associadas.")


class UserHasCommentsException(BusinessException):
    status_code = 409

    def __init__(self):
        super().__init__("Não é possível remover o usuário porque ele possui comentários associados.")


class UserHasPaymentsException(BusinessException):
    status_code = 409

    def __init__(self):
        super().__init__("Não é possível remover o usuário porque ele possui pagamentos associados.")

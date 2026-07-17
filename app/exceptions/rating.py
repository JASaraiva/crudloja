from app.exceptions.business import BusinessException


class RatingNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Avaliação não encontrada.")



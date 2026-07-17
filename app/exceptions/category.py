from app.exceptions.business import BusinessException


class CategoryNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Categoria não encontrada.")

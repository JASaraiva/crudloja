from app.exceptions.business import BusinessException


class ProductNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Produto não encontrado.")

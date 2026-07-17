from app.exceptions.business import BusinessException


class OrderNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Pedido não encontrado.")

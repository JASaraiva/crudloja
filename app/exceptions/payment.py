from app.exceptions.business import BusinessException


class PaymentNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Pagamento não encontrado.")

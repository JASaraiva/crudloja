from app.exceptions.business import BusinessException


class PaymentMethodNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Forma de pagamento não encontrada.")

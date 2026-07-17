from app.exceptions.business import BusinessException


class AdvertisementNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Anúncio não encontrado.")

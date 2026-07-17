from app.exceptions.base import AppException


class BusinessException(AppException):

    status_code = 400

    def __init__(self, message: str):
        super.message = message
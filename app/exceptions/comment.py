from app.exceptions.business import BusinessException


class CommentNotFoundException(BusinessException):
    status_code = 404

    def __init__(self):
        super().__init__("Comentário não encontrado.")

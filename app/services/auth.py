from app.exceptions import UnauthorizedException
from app.repositories import UserRepository
from app.schemas import AuthLogin, TokenSchema
from app.utils import verify_password, create_access_token


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def login(self, credentials: AuthLogin) -> TokenSchema:
        user = self.repository.get_by_email(credentials.email)

        if not user or not verify_password(credentials.password, user.password):
            raise UnauthorizedException()

        token = create_access_token(subject=user.email)
        return TokenSchema(access_token=token, token_type="bearer")

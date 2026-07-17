from app.repositories import RatingRepository
from app.exceptions import RatingNotFoundException
from app.models import Rating
from app.schemas import RatingCreate, RatingUpdate


class RatingService():

    def __init__(self, repository: RatingRepository):
        self.repository = repository

    def get(self, rating_id: int) -> Rating:
        rating = self.repository.get(rating_id)
        if rating is None:
            raise RatingNotFoundException()
        return rating

    def list(self) -> list[Rating]:
        return self.repository.list()

    def create(self, rating_data: RatingCreate) -> Rating:
        return self.repository.create(rating_data)

    def update(self, rating_id: int, rating_data: RatingUpdate) -> Rating:
        updated = self.repository.update(rating_id, rating_data)
        if updated is None:
            raise RatingNotFoundException()
        return updated

    def delete(self, rating_id: int) -> None:
        self.get(rating_id)
        self.repository.delete(rating_id)

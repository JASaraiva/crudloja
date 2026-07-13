from app.repositories import RatingRepository
from app.exceptions import RatingNotFoundException
from app.models import Rating
from app.schemas import RatingCreate


class RatingService():
    
    def __init__(self, repository: RatingRepository):
        self.repository = repository


    def get(self, rating_id: int) -> Rating:

        rating = self.repository.get(rating_id)

        if rating is None:
            raise RatingNotFoundException(rating_id)
        
        return rating
    

    
    def list(self) -> Rating:
        ratings = self.repository.list()
        return ratings
    

    def create(self, rating_data: RatingCreate) -> Rating: 
        return self.repository.create(rating_data)
        

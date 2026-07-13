from app.repositories import RatingRepository
from app.exceptions import RatingNotFoundException
from app.models import Rating
from app.schemas import RatingCreate


class RatingService():
    
    def __init__(self, repository: RatingRepository):
        self.repository = repository


    def get_rating(self, rating_id: int) -> Rating:

        rating = self.repository.get_rating(rating_id)

        if rating is None:
            raise RatingNotFoundException(rating_id)
        
        return rating
    

    
    def list_ratings(self) -> Rating:
        ratings = self.repository.list_ratings()
        return ratings
    

    def create_rating(self, rating_data: RatingCreate) -> Rating: 
        return self.repository.create_rating(rating_data)
        

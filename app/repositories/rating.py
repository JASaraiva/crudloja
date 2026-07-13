from sqlalchemy.orm import Session
from app.models import Rating
from app.repositories.base import BaseRepository
from app.schemas import RatingCreate, RatingUpdate


class RatingRepository(BaseRepository[Rating, RatingCreate, RatingUpdate]):

    def __init__(self, db: Session):
        super().__init__(Rating, db)

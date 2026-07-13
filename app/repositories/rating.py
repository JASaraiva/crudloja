from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Rating
from app.schemas import RatingCreate, RatingUpdate


class RatingRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_rating(self, rating: RatingCreate) -> Rating:
        db_rating = Rating(**rating.model_dump())
        self.db.add(db_rating)
        self.db.commit()
        self.db.refresh(db_rating)
        return db_rating


    def get_rating(self, rating_id: int) -> Rating | None:
        stmt = select(Rating).where(Rating.id == rating_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_ratings(self) -> list[Rating]:
        stmt = select(Rating)
        return self.db.execute(stmt).scalars().all()


    def update_rating(self, rating_id: int, rating_data: RatingUpdate) -> Rating:
        rating = self.get_rating(rating_id)

        for key, value in rating_data.model_dump().items():
            setattr(rating, key, value)
        self.db.commit()
        self.db.refresh(rating)
        return rating


    def delete_rating(self, rating_id: int) -> None:
        rating = self.get_rating(rating_id)
        self.db.delete(rating)
        self.db.commit()

from sqlalchemy.orm import Session

from app.models import Advertisement
from app.repositories.base import BaseRepository
from app.schemas import AdvertisementCreate, AdvertisementUpdate


class AdvertisementRepository(BaseRepository[Advertisement, AdvertisementCreate, AdvertisementUpdate]):

    def __init__(self, db: Session):
        super().__init__(Advertisement, db)

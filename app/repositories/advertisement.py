from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Advertisement
from app.schemas import AdvertisementCreate, AdvertisementUpdate


class AdvertisementRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_advertisement(self, advertisement: AdvertisementCreate) -> Advertisement:
        db_advertisement = Advertisement(**advertisement.model_dump())
        self.db.add(db_advertisement)
        self.db.commit()
        self.db.refresh(db_advertisement)
        return db_advertisement


    def get_advertisement(self, advertisement_id: int) -> Advertisement | None:
        stmt = select(Advertisement).where(Advertisement.id == advertisement_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_advertisements(self) -> list[Advertisement]:
        stmt = select(Advertisement)
        return self.db.execute(stmt).scalars().all()


    def update_advertisement(self, advertisement_id: int, advertisement_data: AdvertisementUpdate) -> Advertisement:
        advertisement = self.get_advertisement(advertisement_id)

        for key, value in advertisement_data.model_dump().items():
            setattr(advertisement, key, value)
        self.db.commit()
        self.db.refresh(advertisement)
        return advertisement


    def delete_advertisement(self, advertisement_id: int) -> None:
        advertisement = self.get_advertisement(advertisement_id)
        self.db.delete(advertisement)
        self.db.commit()

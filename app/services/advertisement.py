from app.repositories import AdvertisementRepository
from app.exceptions import AdvertisementNotFoundException
from app.models import Advertisement
from app.schemas import AdvertisementCreate, AdvertisementUpdate


class AdvertisementService():

    def __init__(self, repository: AdvertisementRepository):
        self.repository = repository

    def get(self, advertisement_id: int) -> Advertisement:
        advertisement = self.repository.get(advertisement_id)
        if advertisement is None:
            raise AdvertisementNotFoundException()
        return advertisement

    def list(self) -> list[Advertisement]:
        return self.repository.list()

    def create(self, advertisement_data: AdvertisementCreate) -> Advertisement:
        return self.repository.create(advertisement_data)

    def update(self, advertisement_id: int, advertisement_data: AdvertisementUpdate) -> Advertisement:
        updated = self.repository.update(advertisement_id, advertisement_data)
        if updated is None:
            raise AdvertisementNotFoundException()
        return updated

    def delete(self, advertisement_id: int) -> None:
        self.get(advertisement_id)
        self.repository.delete(advertisement_id)

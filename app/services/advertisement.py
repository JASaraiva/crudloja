from app.repositories import AdvertisementRepository
from app.exceptions import AdvertisementNotFoundException
from app.models import Advertisement
from app.schemas import AdvertisementCreate


class AdvertisementService():
    
    def __init__(self, repository: AdvertisementRepository):
        self.repository = repository


    def get(self, advertisement_id: int) -> Advertisement:

        advertisement = self.repository.get(advertisement_id)

        if advertisement is None:
            raise AdvertisementNotFoundException(advertisement_id)
        
        return advertisement
    

    
    def list(self) -> Advertisement:
        advertisements = self.repository.list()
        return advertisements
    

    def create(self, advertisement_data: AdvertisementCreate) -> Advertisement: 
        return self.repository.create(advertisement_data)
        

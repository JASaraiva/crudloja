from app.repositories import AdvertisementRepository
from app.exceptions import AdvertisementNotFoundException
from app.models import Advertisement
from app.schemas import AdvertisementCreate


class AdvertisementService():
    
    def __init__(self, repository: AdvertisementRepository):
        self.repository = repository


    def get_advertisement(self, advertisement_id: int) -> Advertisement:

        advertisement = self.repository.get_advertisement(advertisement_id)

        if advertisement is None:
            raise AdvertisementNotFoundException(advertisement_id)
        
        return advertisement
    

    
    def list_advertisements(self) -> Advertisement:
        advertisements = self.repository.list_advertisements()
        return advertisements
    

    def create_advertisement(self, advertisement_data: AdvertisementCreate) -> Advertisement: 
        return self.repository.create_advertisement(advertisement_data)
        

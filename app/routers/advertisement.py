from fastapi import APIRouter, status, Depends
from app.schemas import AdvertisementCreate, AdvertisementUpdate, AdvertisementResponse
from app.services import AdvertisementService
from app.dependencies import get_advertisement_service

router = APIRouter(prefix="/advertisements", tags=["advertisements"])

@router.get("/")
def list_advertisements(service: AdvertisementService = Depends(get_advertisement_service)) -> list[AdvertisementResponse]:
    return service.list_advertisements()

@router.get("/{id}")
def get_advertisement(id: int, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.get_advertisement(id)

@router.post("/", response_model=AdvertisementResponse, status_code=status.HTTP_201_CREATED)
def create_advertisement(advertisement: AdvertisementCreate, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.create_advertisement(advertisement)

@router.put("/{id}", response_model=AdvertisementResponse, status_code=status.HTTP_200_OK)
def update_advertisement(id: int, advertisement: AdvertisementUpdate, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.update_advertisement(id, advertisement)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_advertisement(id: int, service: AdvertisementService = Depends(get_advertisement_service)) -> None:
    service.delete_advertisement(id)

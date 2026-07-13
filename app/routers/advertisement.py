from fastapi import APIRouter, status, Depends
from app.schemas import AdvertisementCreate, AdvertisementUpdate, AdvertisementResponse
from app.services import AdvertisementService
from app.dependencies import get_advertisement_service

router = APIRouter(prefix="/advertisements", tags=["advertisements"])

@router.get("/")
def list(service: AdvertisementService = Depends(get_advertisement_service)) -> list[AdvertisementResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.get(id)

@router.post("/", response_model=AdvertisementResponse, status_code=status.HTTP_201_CREATED)
def create(advertisement: AdvertisementCreate, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.create(advertisement)

@router.put("/{id}", response_model=AdvertisementResponse, status_code=status.HTTP_200_OK)
def update(id: int, advertisement: AdvertisementUpdate, service: AdvertisementService = Depends(get_advertisement_service)) -> AdvertisementResponse:
    return service.update(id, advertisement)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: AdvertisementService = Depends(get_advertisement_service)) -> None:
    service.delete(id)

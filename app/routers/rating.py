from fastapi import APIRouter, status, Depends

from app.schemas import RatingCreate, RatingUpdate, RatingResponse
from app.services import RatingService
from app.dependencies import get_rating_service

router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.get("/")
def list(service: RatingService = Depends(get_rating_service)) -> list[RatingResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.get(id)

@router.post("/", response_model=RatingResponse, status_code=status.HTTP_201_CREATED)
def create(rating: RatingCreate, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.create(rating)

@router.put("/{id}", response_model=RatingResponse, status_code=status.HTTP_200_OK)
def update(id: int, rating: RatingUpdate, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.update(id, rating)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: RatingService = Depends(get_rating_service)) -> None:
    service.delete(id)

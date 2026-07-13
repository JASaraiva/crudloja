from fastapi import APIRouter, status, Depends
from app.schemas import RatingCreate, RatingUpdate, RatingResponse
from app.services import RatingService
from app.dependencies import get_rating_service

router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.get("/")
def list_ratings(service: RatingService = Depends(get_rating_service)) -> list[RatingResponse]:
    return service.list_ratings()

@router.get("/{id}")
def get_rating(id: int, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.get_rating(id)

@router.post("/", response_model=RatingResponse, status_code=status.HTTP_201_CREATED)
def create_rating(rating: RatingCreate, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.create_rating(rating)

@router.put("/{id}", response_model=RatingResponse, status_code=status.HTTP_200_OK)
def update_rating(id: int, rating: RatingUpdate, service: RatingService = Depends(get_rating_service)) -> RatingResponse:
    return service.update_rating(id, rating)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(id: int, service: RatingService = Depends(get_rating_service)) -> None:
    service.delete_rating(id)

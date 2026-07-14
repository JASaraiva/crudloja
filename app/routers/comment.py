from fastapi import APIRouter, status, Depends

from app.schemas import CommentCreate, CommentUpdate, CommentResponse
from app.services import CommentService
from app.dependencies import get_comment_service

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/")
def list(service: CommentService = Depends(get_comment_service)) -> list[CommentResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.get(id)

@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create(comment: CommentCreate, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.create(comment)

@router.put("/{id}", response_model=CommentResponse, status_code=status.HTTP_200_OK)
def update(id: int, comment: CommentUpdate, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.update(id, comment)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: CommentService = Depends(get_comment_service)) -> None:
    service.delete(id)

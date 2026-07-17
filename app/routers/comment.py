from fastapi import APIRouter, Depends, status

from app.dependencies import get_current_user, get_comment_service
from app.schemas import CommentCreate, CommentUpdate, CommentResponse
from app.services import CommentService

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    dependencies=[Depends(get_current_user)],
)


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

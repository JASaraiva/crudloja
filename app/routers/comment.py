from fastapi import APIRouter, status, Depends
from app.schemas import CommentCreate, CommentUpdate, CommentResponse
from app.services import CommentService
from app.dependencies import get_comment_service

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/")
def list_comments(service: CommentService = Depends(get_comment_service)) -> list[CommentResponse]:
    return service.list_comments()

@router.get("/{id}")
def get_comment(id: int, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.get_comment(id)

@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(comment: CommentCreate, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.create_comment(comment)

@router.put("/{id}", response_model=CommentResponse, status_code=status.HTTP_200_OK)
def update_comment(id: int, comment: CommentUpdate, service: CommentService = Depends(get_comment_service)) -> CommentResponse:
    return service.update_comment(id, comment)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(id: int, service: CommentService = Depends(get_comment_service)) -> None:
    service.delete_comment(id)

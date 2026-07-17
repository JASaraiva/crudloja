from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CommentBase(BaseModel):
    title: str = Field(min_length=3, max_length=100, examples=["Ótimo produto"])
    text: str = Field(min_length=5, max_length=255)
    user_id: int = Field(gt=0, examples=[1])


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

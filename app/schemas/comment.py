from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class CommentBase(BaseModel):
    title: str = Field(min_length=3, max_length=100, examples=["Eletrônicos"])
    text: str = Field(min_length=5, max_length=255)
    user_id: int = Field(gt=0, examples=[1])
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
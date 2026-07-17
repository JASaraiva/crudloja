from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["John Doe"])
    email: str = Field(min_length=5, max_length=255, examples=["john.doe@example.com"])


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=72, examples=["a6a78aiajhas$*&afa"])


class UserUpdate(UserBase):
    password: str | None = Field(default=None, min_length=6, max_length=72, examples=["a6a78aiajhas$*&afa"])


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

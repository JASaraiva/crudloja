from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Eletrônicos"])
    description: str = Field(min_length=5, max_length=255)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(
        from_attributes=True,
    )
from pydantic import BaseModel, ConfigDict, Field


## Schemas for Category
class CategoryBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Eletrônicos"])

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True
    )

class CategoryUpdate(CategoryBase):
    pass

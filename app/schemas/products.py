from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from .categories import CategoryResponse

## Schemas for Product
class ProductBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Notebook Dell"])
    description: str = Field(min_length=5, max_length=255)
    value: Decimal = Field(gt=0, decimal_places=2)
    category_id: int = Field(gt=0, examples=[1])
    stock: int = Field(ge=0, examples=[10])

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):

    id: int
    category: CategoryResponse
    model_config = ConfigDict(
            from_attributes=True,
    )


class ProductUpdate(ProductBase):
    pass

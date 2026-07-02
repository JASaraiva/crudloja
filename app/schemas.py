from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal


class ProductBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Notebook Dell"])
    description: str = Field(min_length=5, max_length=255)
    value: Decimal = Field(gt=0, decimal_places=2)

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):

    id: int

    model_config = ConfigDict(
            from_attributes=True
    )

class ProductUpdate(ProductBase):
    pass

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    value: float

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):

    id: int

    model_config = ConfigDict(
            from_attributes=True
    )


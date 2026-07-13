from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal

class RatingBase(BaseModel):
    user_id: int = Field(gt=0, examples=[1])
    product_id: int = Field(gt=0, examples=[1])
    value: int = Field(ge=0, examples=[10])

class RatingCreate(RatingBase):
    pass

class RatingUpdate(RatingBase):
    pass

class RatingResponse(RatingBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
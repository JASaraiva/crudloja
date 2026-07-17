from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class OrderBase(BaseModel):
    product_id: int = Field(gt=0, examples=[1])
    status: int = Field(ge=0, examples=[0])


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

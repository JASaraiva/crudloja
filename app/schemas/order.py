from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class OrderBase(BaseModel):
    product_id: int = Field(gt=0, examples=[1])
    status: str = Field(min_length=3, max_length=100, examples=["Pendente"])
    created_at: datetime     = Field(default_factory=datetime.utcnow)

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
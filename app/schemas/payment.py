from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class PaymentBase(BaseModel):
    payment_method_id: int = Field(gt=0, examples=[1])
    user_id: int = Field(gt=0, examples=[1])
    order_id: int = Field(gt=0, examples=[1])
    status: int = Field(gt=-1, examples=[1])

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
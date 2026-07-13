from pydantic import BaseModel, ConfigDict, Field

class PaymentMethodBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Eletrônicos"])
    description: str = Field(min_length=5, max_length=255)

class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodUpdate(PaymentMethodBase):
    pass

class PaymentMethodResponse(PaymentMethodBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
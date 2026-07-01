from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    value: float


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    value: float
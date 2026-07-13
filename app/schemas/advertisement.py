from pydantic import BaseModel, ConfigDict, Field


class AdvertisementBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Eletrônicos"])
    description: str = Field(min_length=5, max_length=255)


class AdvertisementCreate(AdvertisementBase):
    pass


class AdvertisementUpdate(AdvertisementBase):
    pass


class AdvertisementResponse(AdvertisementBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
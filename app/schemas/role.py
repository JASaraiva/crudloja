from pydantic import BaseModel, ConfigDict, Field

class RoleBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, examples=["Administrador"])
   

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int
    model_config = ConfigDict(
            from_attributes=True,
    )
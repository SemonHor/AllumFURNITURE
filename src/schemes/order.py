from pydantic import BaseModel, Field, UUID4


class OrderCreate(BaseModel):
    status: str = Field(description="Status", default=None)
    client_uid: UUID4 = Field(description="UUID")


class OrderFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    status: str = Field(description="Status", default=None)
    client_uid: UUID4 = Field(description="UUID")

from pydantic import BaseModel, Field, UUID4
from typing import Optional


class OrderCreate(BaseModel):
    status: str = Field(description="Status", default=None)
    client_uid: Optional[UUID4] = Field(description="UUID", default=None)


class OrderFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    status: str = Field(description="Status", default=None)
    client_uid: Optional[UUID4] = Field(description="UUID")


class OrderFromFilter(BaseModel):
    uid: Optional[UUID4] = Field(description="UUID")
    status: Optional[str] = Field(description="Status", default=None)
    client_uid: Optional[UUID4] = Field(description="UUID", default=None)

from pydantic import BaseModel, Field, UUID4
from typing import Optional


class ClientCreate(BaseModel):
    email: str = Field(description="Client email", default=None)
    phone_number: str = Field(description="Client phone number", default=None, nullable=True)


class ClientFromDB(BaseModel):
    uid: UUID4 = Field(description="Furniture ID", default=None)
    email: str = Field(description="Client email", default=None, nullable=True)
    phone_number: str = Field(description="Client phone number", default=None, nullable=True)


class ClientFromFilter(BaseModel):
    max_outputs: Optional[int]
    uid: Optional[UUID4]
    email: Optional[str]
    phone_number: Optional[str]

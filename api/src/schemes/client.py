from pydantic import BaseModel, Field, UUID4
from typing import Optional


class ClientCreate(BaseModel):
    first_name: str = Field(description="Client first name", default=None)
    last_name: str = Field(description="Client last name", default=None)
    email: str = Field(description="Client email", default=None)
    phone_number: str = Field(description="Client phone number", default=None, nullable=True)


class ClientFromDB(BaseModel):
    uid: UUID4 = Field(description="Furniture ID", default=None)
    first_name: str = Field(description="Client first name", default=None)
    last_name: str = Field(description="Client last name", default=None)
    email: str = Field(description="Client email", default=None, nullable=True)
    phone_number: str = Field(description="Client phone number", default=None, nullable=True)


class ClientFromFilter(BaseModel):
    limit: Optional[int] = Field(default=100, ge=0, le=1000, nullable=True)
    offset: Optional[int] = Field(default=0, ge=0, nullable=True)
    first_name: Optional[str] = Field(default=None, nullable=True)
    last_name: Optional[str] = Field(default=None, nullable=True)
    email: Optional[str] = Field(default=None, nullable=True)
    phone_number: Optional[str] = Field(default=None, nullable=True)

from pydantic import BaseModel, Field, UUID4
from typing import Optional


class MaterialCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Material in...")


class MaterialFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Material in...")


class MaterialFromFilter(BaseModel):
    uid: Optional[UUID4] = Field(default=None, nullable=True)
    name: Optional[str] = Field(default=None, nullable=True)
    uid_part: Optional[UUID4] = Field(default=None, nullable=True)

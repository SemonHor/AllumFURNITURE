from pydantic import BaseModel, Field, UUID4
from typing import Optional


class PartPreformCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Standard for...", default=None)


class PartPreformFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Standard for...", default=None)


class PartPreformFromFilter(BaseModel):
    max_outputs: Optional[int]
    uid: Optional[UUID4]
    name: Optional[str]
    uid_part: Optional[UUID4]

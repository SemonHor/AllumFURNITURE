from pydantic import BaseModel, Field, UUID4
from typing import Optional


class PartCreate(BaseModel):
    uid_furniture: UUID4 | None = Field(description="Part in...")


class PartFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    uid_furniture: UUID4 | None = Field(description="Part in...")


class PartFromFilter(BaseModel):
    max_outputs: Optional[int]
    uid: Optional[UUID4]
    uid_furniture: Optional[UUID4]

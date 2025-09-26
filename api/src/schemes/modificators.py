from pydantic import BaseModel, Field, UUID4
from typing import Optional


class ModificatorCreate(BaseModel):
    name: str = Field(description="Status", default=None)
    value: float = Field(description="Value", default=None)
    uid_part: UUID4 | None = Field(description="Included in...", default=None)


class ModificatorFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str = Field(description="Modificator name", default=None)
    description: str = Field(description="Modificator name", default=None)
    value: float = Field(description="Value", default=None)
    uid_part: UUID4 | None = Field(description="Included in...", default=None)


class ModificatorFromFilter(BaseModel):
    uid: Optional[UUID4]
    name: Optional[str]
    uid_part: Optional[UUID4]

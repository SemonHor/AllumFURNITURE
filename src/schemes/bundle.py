from pydantic import BaseModel, Field, UUID4
from typing import Optional


class BundleCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None, nullable=True)
    photos_link: str | None = Field(description="Link to photos", default=None, nullable=True)
    is_standart: bool = Field(description="Is standart bundle", default=False)
    uid_order: UUID4 | None = Field(description="Included in...", default=None, nullable=True)


class BundleFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    photos_link: str | None = Field(description="Link to photos", default=None)
    is_standart: bool = Field(description="Is standart bundle", default=False)
    uid_order: UUID4 | None = Field(description="Included in...", default=None, nullable=True)


# ia - is_available...
# iс - in_certain...
class BundleFromFilter(BaseModel):
    max_outputs: Optional[int] = Field(default=None)
    uid: Optional[UUID4] = Field(default=None)
    name: Optional[str] = Field(default=None)
    ia_photos_link: Optional[bool] = Field(default=None)
    is_standart: Optional[bool] = Field(default=None)
    in_order: Optional[bool] = Field(default=None)
    iс_order: Optional[UUID4] = Field(default=None)

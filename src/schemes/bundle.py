from pydantic import BaseModel, Field, UUID4


class BundleCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    photos_link: str | None = Field(description="Link to photos", default=None)
    is_standart: bool = Field(description="Is standart bundle", default=False)
    uid_order: UUID4 | None = Field(description="Included in...", default=None, nullable=True)


class BundleFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    photos_link: str | None = Field(description="Link to photos", default=None)
    is_standart: bool = Field(description="Is standart bundle", default=False)
    uid_order: UUID4 | None = Field(description="Included in...", default=None)

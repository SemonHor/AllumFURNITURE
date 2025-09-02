from pydantic import BaseModel, Field, UUID4


class FurnitureCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    photos_link: str | None = Field(description="Link to photos", default=None)
    uid_order: UUID4 | None = Field(description="Included in...")
    uid_bundle: UUID4 | None = Field(description="Included in...")


class FurnitureFromDB(BaseModel):
    uid: UUID4 = Field(description="Furniture ID", default=None)
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    photos_link: str | None = Field(description="Link to photos", default=None)
    uid_order: UUID4 | None = Field(description="Included in...")
    uid_bundle: UUID4 | None = Field(description="Included in...")

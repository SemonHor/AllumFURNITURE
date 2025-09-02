from pydantic import BaseModel, Field, UUID4


class MatterialCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Material in...")


class MatterialFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Material in...")

from pydantic import BaseModel, Field, UUID4


class StadartPartCreate(BaseModel):
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Standard for...")


class StandartPartFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    name: str | None = Field(description="Name", default=None)
    description: str | None = Field(description="Description", default=None)
    uid_part: UUID4 | None = Field(description="Standard for...")

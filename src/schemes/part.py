from pydantic import BaseModel, Field, UUID4


class PartCreate(BaseModel):
    uid_furniture: UUID4 | None = Field(description="Part in...")


class PartFromDB(BaseModel):
    uid: UUID4 = Field(description="UUID")
    uid_furniture: UUID4 | None = Field(description="Part in...")

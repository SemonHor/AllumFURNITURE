from pydantic import BaseModel, Field, UUID4


class ClientCreate(BaseModel):
    email: str = Field(description="Client email", default=None)
    phone_number: str = Field(description="Client phone number", default=None)
    order_uid: UUID4 | None = Field(description="Customer in...")


class ClientFromDB(BaseModel):
    uid: UUID4 = Field(description="Furniture ID", default=None)
    email: str = Field(description="Client email", default=None)
    phone_number: str = Field(description="Client phone number", default=None)
    order_uid: UUID4 | None = Field(description="Customer in...")

from pydantic import BaseModel, Field, ConfigDict


class FurniturePartScheme(BaseModel):
    part_name: str | None = Field(description="Part name", default=None)
    part_id: int | None = Field(description="Part ID", default=None)
    cost: float | None = Field(description="Cost part", default=None)
    modificators: dict[str,float] | None = Field(description="Modificators", default=None)

class FurnitureInputScheme(BaseModel):
    furniture_name: str | None = Field(description="Name", default=None)
    furniture_id: int | None =Field(description="Furniture ID", default=None)
    parts: list[FurniturePartScheme] | None = Field(description="Parts", default=None)


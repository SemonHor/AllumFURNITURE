from pydantic import BaseModel, Field, UUID4
from typing import Optional


class FurnitureCreate(BaseModel):
    name: Optional[str] = Field(default=None, description="Название предмета мебели.")
    description: Optional[str] = Field(default=None, description="Описание предмета мебели.")
    photos_link: Optional[str] = Field(default=None, description="Ссылка на фотографию предмета мебели.")
    uid_order: Optional[UUID4] = Field(default=None, description="Идентификатор заказа.")
    uid_bundle: Optional[UUID4] = Field(default=None, description="Идентификатор набора.")


class FurnitureFromDB(BaseModel):
    uid: UUID4 = Field(description="Идентификатор предмета мебели.")
    name: Optional[str] = Field(default=None, description="Название предмета мебели.")
    description: Optional[str] = Field(default=None, description="Описание предмета мебели.")
    photos_link: Optional[str] = Field(default=None, description="Ссылка на фотографию предмета мебели.")
    uid_order: Optional[UUID4] = Field(default=None, description="Идентификатор заказа.")
    uid_bundle: Optional[UUID4] = Field(default=None, description="Идентификатор набора.")


# ia для фильтров - is_available...
# iс для фильтров - in_certain...
class FurnitureFromFilter(BaseModel):
    max_outputs: Optional[int] = Field(default=None, description="Количество выводимых(max).")
    uid: Optional[UUID4] = Field(description="Идентификатор предмета мебели.")
    name: Optional[str] = Field(default=None, description="Название предмета мебели.")
    ia_photos_link: Optional[bool] = Field(default=None, description="Имеется ссылка на фотографии.")
    in_order: Optional[bool] = Field(default=None, description="Имеется в заказе.")
    iс_order: Optional[UUID4] = Field(default=None, description="Имеется в определённом заказе.")
    in_bundle: Optional[bool] = Field(default=None, description="Имеется в наборе.")
    iс_bundle: Optional[UUID4] = Field(default=None, description="Имеется в определённом наборе.")

import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.schemes.furniture import FurnitureFromDB


class Furniture(Base):
    __tablename__ = 'furniture'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    photos_link: Mapped[str] = mapped_column(String, nullable=False)

    def serialize(self) -> FurnitureFromDB:
        return FurnitureFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            photos_link=self.photos_link,
            uid_order=self.uid_order,
        )

import uuid

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.schemes.furniture import FurnitureFromDB


class Furniture(Base):
    __tablename__ = 'furniture'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    photos_link: Mapped[str] = mapped_column(String, nullable=True)
    uid_order: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('order.uid'), default=None, nullable=True)
    uid_bundle: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('bundle.uid'), default=None, nullable=True)

    def serialize(self) -> FurnitureFromDB:
        return FurnitureFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            photos_link=self.photos_link,
            uid_order=self.uid_order,
            uid_bundle=self.uid_bundle,
        )

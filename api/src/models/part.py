import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.part import PartFromDB


class Part(Base):
    __tablename__ = 'part'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_furniture: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('furniture.uid'), default=None)

    included = relationship("Furniture", backref="parts")

    def serialize(self) -> PartFromDB:
        return PartFromDB(
            uid=self.uid,
            furniture_uid=self.furniture_uid,
        )

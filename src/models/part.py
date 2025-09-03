import uuid

from sqlalchemy import UUID, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.part import PartFromDB
from src.schemes.part_preform import StandartPartFromDB
from src.schemes.materials import MatterialFromDB
from src.schemes.modificators import ModificatorFromDB


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


class PartPreform(Base):
    __tablename__ = 'part_preform'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    part_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None)

    included = relationship("Part", backref="part_preform")

    def serialize(self) -> StandartPartFromDB:
        return StandartPartFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            uid_part=self.uid_part,
        )


class Metarial(Base):
    __tablename__ = 'material'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    uid_part: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None)

    included = relationship("Part", backref="material")

    def serialize(self) -> MatterialFromDB:
        return MatterialFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            uid_part=self.uid_part,
        )


class Modificator(Base):
    __tablename__ = 'modificators'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    uid_part: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None)

    included = relationship("Part", backref="modificators")

    def serialize(self) -> ModificatorFromDB:
        return ModificatorFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            value=self.value,
            uid_part=self.uid_part,
        )

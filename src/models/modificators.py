import uuid

from sqlalchemy import UUID, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.modificators import ModificatorFromDB


class Modificator(Base):
    __tablename__ = 'modificator'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    value: Mapped[float] = mapped_column(Float, nullable=True)
    uid_part: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None, nullable=True)

    included = relationship("Part", backref="modificators")

    def serialize(self) -> ModificatorFromDB:
        return ModificatorFromDB(
            uid=str(self.uid),
            name=self.name,
            description=self.description,
            value=self.value,
            uid_part=self.uid_part,
        )


class ModificatorPartRelations(Base):
    __tablename__ = 'modificator_to_part'
    __table_args__ = (UniqueConstraint('uid_modificator', 'uid_part', name='_modificator_to_part'),)

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_modificator: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('modificator.uid'), default=None)
    uid_part: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None)
    value: Mapped[float] = mapped_column(Float, nullable=False)

    included_modificator = relationship("Modificator", backref="relationsM")
    included_part = relationship("Part", backref="relationsM")

import uuid

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.materials import MaterialFromDB


class Meterial(Base):
    __tablename__ = 'material'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    uid_part: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None)

    included = relationship("Part", backref="material")

    def serialize(self) -> MaterialFromDB:
        return MaterialFromDB(
            uid=str(self.uid),
            name=self.name,
            description=self.description,
            uid_part=self.uid_part
        )

import uuid

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.partpreform import PartPreformFromDB


class PartPreform(Base):
    __tablename__ = 'part_preform'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    part_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('part.uid'), default=None, nullable=True)

    included = relationship("Part", backref="part_preform")

    def serialize(self) -> PartPreformFromDB:
        return PartPreformFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            uid_part=self.uid_part,
        )

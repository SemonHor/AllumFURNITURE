import uuid

from sqlalchemy import UUID, String, Integer, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.bundle import BundleFromDB


class Bundle(Base):
    __tablename__ = 'bundle'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    photos_link: Mapped[str] = mapped_column(String, nullable=True)
    is_standart: Mapped[bool] = mapped_column(Boolean, default=False)
    uid_order: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('order.uid'), default=None, nullable=True)

    included = relationship("Order", backref="bundles")

    def serialize(self) -> BundleFromDB:
        return BundleFromDB(
            uid=self.uid,
            name=self.name,
            description=self.description,
            photos_link=self.photos_link,
            uid_order=self.uid_order,
        )


class FurnitureBundleRelations(Base):
    __tablename__ = 'furniture_to_bundle'
    __table_args__ = (UniqueConstraint('uid_bundle', 'uid_furniture', name='_furniture_to_bundle'),)

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_bundle: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('bundle.uid'), default=None)
    uid_furniture: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('furniture.uid'), default=None)
    furniture_count: Mapped[int] = mapped_column(Integer, default=1)

    included_bundle = relationship("Bundle", backref="relations")
    included_furniture = relationship("Furniture", backref="relations")

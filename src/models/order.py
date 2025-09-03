import uuid

from sqlalchemy import UUID, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, UniqueConstraint

from src.db import Base
from src.schemes.order import OrderFromDB
from src.schemes.order import BundleFromDB


class Order(Base):
    __tablename__ = 'order'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    status: Mapped[str] = mapped_column(String, nullable=False)
    client_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('client.uid'), default=None)

    included = relationship("Client", backref="orders")

    def serialize(self) -> OrderFromDB:
        return OrderFromDB(
            uid=self.uid,
            status=self.status,
            client_uid=self.client_uid,
        )


class Bundle(Base):
    __tablename__ = 'bundle'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    photos_link: Mapped[str] = mapped_column(String, nullable=True)
    is_standart: Mapped[bool] = mapped_column(Boolean, nullable=True)
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
    furniture_count: Mapped[int] = mapped_column(Integer, nullable=False)

    included_bundle = relationship("Bundle", backref="relations")
    included_furniture = relationship("Furniture", backref="relations")

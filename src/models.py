import uuid

from sqlalchemy import UUID, String, Integer, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.client import ClientFromDB
from src.schemes.order import OrderFromDB
from src.schemes.bundle import BundleFromDB
from src.schemes.furniture import FurnitureFromDB
from src.schemes.part import PartFromDB
from src.schemes.part_preform import StandartPartFromDB
from src.schemes.materials import MatterialFromDB
from src.schemes.modificators import ModificatorFromDB


class Client(Base):
    __tablename__ = 'client'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    def serialize(self) -> ClientFromDB:
        return ClientFromDB(
            uid=self.uid,
            email=self.email,
            phone_number=self.phone_number,
        )


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

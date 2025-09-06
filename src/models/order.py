import uuid

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.schemes.order import OrderFromDB


class Order(Base):
    __tablename__ = 'order'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    status: Mapped[str] = mapped_column(String, nullable=True)
    client_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('client.uid'), default=None)

    included = relationship("Client", backref="orders")

    def serialize(self) -> OrderFromDB:
        return OrderFromDB(
            uid=self.uid,
            status=self.status,
            client_uid=self.client_uid,
        )

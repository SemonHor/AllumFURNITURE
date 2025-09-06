import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.schemes.client import ClientFromDB


class Client(Base):
    __tablename__ = 'client'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)

    def serialize(self) -> ClientFromDB:
        return ClientFromDB(
            uid=self.uid,
            email=self.email,
            phone_number=self.phone_number,
        )

import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.schemes.client import ClientFromDB


class Client(Base):
    __tablename__ = 'client'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)

    def serialize(self) -> ClientFromDB:
        return ClientFromDB(
            uid=self.uid,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone_number=self.phone_number
        )

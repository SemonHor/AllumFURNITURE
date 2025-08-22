from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base

class Part(Base):
    __tablename__ = 'Part'

    pid: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    # TODO Здесь должна быть modificators
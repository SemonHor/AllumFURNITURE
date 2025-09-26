from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.config import settings

engine = create_async_engine(url=settings.DB.SQLALCHEMY_DATABASE_URI)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
Base = declarative_base()


async def get_session() -> AsyncSession:  # pyright: ignore[reportInvalidTypeForm]
    async with async_session_maker() as session:
        yield session

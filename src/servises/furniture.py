
from src.models.furniture import Furniture
from src.schemes.furniture import FurnitureCreate, FurnitureFromDB, FurnitureFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class FurnitureService:
    @staticmethod
    async def create(body: FurnitureCreate, db_session) -> FurnitureFromDB:
        query = Furniture(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query

    @staticmethod
    async def update(body: FurnitureFromDB, db_session) -> FurnitureFromDB:
        query = await db_session.execute(select(Furniture).where(Furniture.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query

    @staticmethod
    async def filter(filters: FurnitureFromFilter, db_session):
        pass

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Furniture).where(Furniture.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

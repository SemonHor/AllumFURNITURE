from src.models.part import Part
from src.schemes.part import PartCreate, PartFromDB, PartFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class PartService:
    @staticmethod
    async def create(body: PartCreate, db_session) -> PartFromDB:
        query = Part(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query

    @staticmethod
    async def update(body: PartFromDB, db_session) -> PartFromDB:
        query = await db_session.execute(select(Part).where(Part.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query

    @staticmethod
    async def filter(filters: PartFromFilter, db_session):
        pass

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Part).where(Part.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

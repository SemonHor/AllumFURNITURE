from src.models.bundle import Bundle
from src.schemes.bundle import BundleCreate, BundleFromDB, BundleFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class BundleService:
    @staticmethod
    async def create(body: BundleCreate, db_session) -> BundleFromDB:
        query = Bundle(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def update(body: BundleFromDB, db_session) -> BundleFromDB:
        query = await db_session.execute(select(Bundle).where(Bundle.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def filter(body: BundleFromFilter, db_session):
        pass

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Bundle).where(Bundle.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

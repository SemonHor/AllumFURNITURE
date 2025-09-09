from src.models.partpreform import PartPreform
from src.schemes.partpreform import PartPreformCreate, PartPreformFromDB, PartPreformFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class PartPreformService:
    @staticmethod
    async def create(body: PartPreformCreate, db_session):
        query = PartPreform(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query

    @staticmethod
    async def update(body: PartPreformFromDB, db_session):
        query = await db_session.execute(select(PartPreform).where(PartPreform.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query

    @staticmethod
    async def filter(filters: PartPreformFromFilter, db_session):
        pass

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(PartPreform).where(PartPreform.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

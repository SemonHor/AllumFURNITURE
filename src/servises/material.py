from src.models.material import Meterial
from src.schemes.materials import MaterialCreate, MaterialFromDB, MaterialFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class MatherialService:
    @staticmethod
    async def create(body: MaterialCreate, db_session) -> MaterialFromDB:
        query = Meterial(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def update(body: MaterialFromDB, db_session) -> MaterialFromDB:
        query = await db_session.execute(select(Meterial).where(Meterial.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def filter(filters: MaterialFromFilter, db_session):
        pass

    @staticmethod
    async def delete_f(uid: UUID4, db_session):
        stmt = delete(Meterial).where(Meterial.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

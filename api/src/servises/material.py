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
        query = select(Meterial)

        if filters.name is not None:
            query = query.where(Meterial.name.uid == filters.uid)
        if filters.uid is not None:
            query = query.where(Meterial.uid.ilike(f'%{filters.uid}%'))
        if filters.uid_part is not None:
            query = query.where(Meterial.uid_part == filters.uid_part)

        query = query.limit(filters.limit).offset(filters.offset)

        result = await db_session.execute(query)
        clients = result.scalars().all()
        return [client.serialize() for client in clients]

    @staticmethod
    async def delete_f(uid: UUID4, db_session):
        stmt = delete(Meterial).where(Meterial.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

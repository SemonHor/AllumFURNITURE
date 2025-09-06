from src.models.modificators import Modificator
from src.schemes.modificators import ModificatorCreate, ModificatorFromDB, ModificatorFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class ModificatorService:
    # Здесь происходит создание part
    async def create(body: ModificatorCreate, db_session):
        query = Modificator(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        return query.serialize()


    # Здесь происходит обновление тех или иных данных в part
    async def update(body: ModificatorFromDB, db_session):
        query = await db_session.execute(select(Modificator).where(Modificator.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
        else:
            raise Exception("not found")
        return query


    async def filter(filters: ModificatorFromFilter, db_session):
        pass


    # Здесь происходит удаление тех или иных данных в furniture
    async def delete_f(uid: UUID4, db_session):
        stmt = delete(Modificator).where(Modificator.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

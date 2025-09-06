from src.models.material import Meterial
from src.schemes.materials import MaterialCreate, MaterialFromDB, MaterialFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


# Здесь происходит создание part
async def create(body: MaterialCreate, db_session):
    query = Meterial(**body.model_dump(exclude_unset=True))
    db_session.add(query)
    await db_session.commit()
    return query


# Здесь происходит обновление тех или иных данных в part
async def update(body: MaterialFromDB, db_session):
    query = await db_session.execute(select(Meterial).where(Meterial.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        return query.scalars()


async def filter(filters: MaterialFromFilter, db_session):
    pass


# Здесь происходит удаление тех или иных данных в furniture
async def delete_f(uid: UUID4, db_session):
    stmt = delete(Meterial).where(Meterial.uid == uid)
    await db_session.execute(stmt)
    await db_session.commit()

from src.models.client import Client
from src.schemes.client import ClientCreate, ClientFromDB, ClientFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


# Здесь происходит создание client
async def create(body: ClientCreate, db_session) -> ClientFromDB:
    query = Client(**body.model_dump(exclude_unset=True))
    db_session.add(query)
    await db_session.commit()
    return query


# Здесь происходит обновление тех или иных данных в client
async def update(body: ClientFromDB, db_session) -> ClientFromDB:
    query = await db_session.execute(select(Client).where(Client.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        return query


# Здесь находится нахождение по фильтрам client
async def filter(filters: ClientFromFilter, db_session):
    pass


# Здесь происходит удаление тех или иных данных в client
async def delete_f(uid: UUID4, db_session):
    stmt = delete(Client).where(Client.uid == uid)
    await db_session.execute(stmt)
    await db_session.commit()

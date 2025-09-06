# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession
from src.models.furniture import Furniture
from src.schemes.furniture import FurnitureCreate, FurnitureFromDB, FurnitureFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


# Здесь происходит создание furniture
async def create(body: FurnitureCreate, db_session):
    furniture = Furniture(**body.model_dump(exclude_unset=True))
    db_session.add(furniture)
    await db_session.commit()
    return furniture


# Здесь происходит обновление тех или иных данных в furniture
async def update(body: FurnitureFromDB, db_session):
    query = await db_session.execute(select(Furniture).where(Furniture.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        return query.scalars()


# Здесь находится нахождение по фильтрам furniture
async def filter(filters: FurnitureFromFilter, db_session):
    pass


# Здесь происходит удаление тех или иных данных в furniture
async def delete_f(uid: UUID4, db_session):
    stmt = delete(Furniture).where(Furniture.uid == uid)
    await db_session.execute(stmt)
    await db_session.commit()

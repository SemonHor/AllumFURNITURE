from src.models.bundle import Bundle
from src.schemes.bundle import BundleCreate, BundleFromDB, BundleFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


# Здесь происходит создание bundle
async def create(body: BundleCreate, db_session) -> BundleFromDB:
    furniture = Bundle(**body.model_dump(exclude_unset=True))
    db_session.add(furniture)
    await db_session.commit()
    return furniture


# Здесь происходит обновление тех или иных данных в bundle
async def update(body: BundleFromDB, db_session) -> BundleFromDB:
    query = await db_session.execute(select(Bundle).where(Bundle.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        return query.scalars()


# Здесь происходит нахождение тех или иных данных в bundle
async def filter(body: BundleFromFilter, db_session):
    pass


# Здесь происходит удаление тех или иных данных из bundle
async def delete_f(uid: UUID4, db_session):
    stmt = delete(Bundle).where(Bundle.uid == uid)
    await db_session.execute(stmt)
    await db_session.commit()

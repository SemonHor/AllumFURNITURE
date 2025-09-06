# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession
from src.models.order import Order
from src.schemes.order import OrderCreate, OrderFromDB, OrderFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


# Здесь происходит создание order
async def create(body: OrderCreate, db_session) -> OrderFromDB:
    order = Order(**body.model_dump(exclude_unset=True))
    db_session.add(order)
    await db_session.commit()
    return order


# Здесь происходит обновление тех или иных данных в order
async def update(body: OrderFromDB, db_session) -> OrderFromDB:
    query = await db_session.execute(select(Order).where(Order.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        return query.scalars()


# Здесь происходит нахождение тех или иных данных в bundle
async def filter(body: OrderFromFilter, db_session):
    pass


# Здесь происходит удаление тех или иных данных в order
async def delete_f(uid: UUID4, db_session):
    stmt = delete(Order).where(Order.uid == uid)
    await db_session.execute(stmt)
    await db_session.commit()

from src.models.order import Order
from src.schemes.order import OrderCreate, OrderFromDB, OrderFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class OrderService:
    @staticmethod
    async def create(body: OrderCreate, db_session) -> OrderFromDB:
        query = Order(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query

    @staticmethod
    async def update(body: OrderFromDB, db_session) -> OrderFromDB:
        query = await db_session.execute(select(Order).where(Order.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query

    @staticmethod
    async def filter(body: OrderFromFilter, db_session):
        pass

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Order).where(Order.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

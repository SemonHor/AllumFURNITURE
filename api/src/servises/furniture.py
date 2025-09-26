
from src.models.furniture import Furniture
from src.schemes.furniture import FurnitureCreate, FurnitureFromDB, FurnitureFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class FurnitureService:
    @staticmethod
    async def create(body: FurnitureCreate, db_session) -> FurnitureFromDB:
        query = Furniture(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query

    @staticmethod
    async def update(body: FurnitureFromDB, db_session) -> FurnitureFromDB:
        query = await db_session.execute(select(Furniture).where(Furniture.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query

    @staticmethod
    async def filter(filters: FurnitureFromFilter, db_session):
        query = select(Furniture)

        if filters.name is not None:
            query = query.where(Furniture.name.ilike(f'%{filters.first_name}%'))
        if filters.uid is not None:
            query = query.where(Furniture.uid.ilike(f'%{filters.uid}%'))
        if filters.ia_photos_link is not None:
            query = query.where(Furniture.photos_link is not None)
        if filters.in_order is not None:
            query = query.where(Furniture.uid_order is not None)
        if filters.iс_order is not None:
            query = query.where(Furniture.uid_order == filters.iс_order)
        if filters.in_bundle is not None:
            query = query.where(Furniture.uid_bundle is not None)
        if filters.ic_bundle is not None:
            query = query.where(Furniture.uid_bundle == filters.ic_bundle)

        query = query.limit(filters.limit).offset(filters.offset)

        result = await db_session.execute(query)
        clients = result.scalars().all()
        return [client.serialize() for client in clients]

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Furniture).where(Furniture.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

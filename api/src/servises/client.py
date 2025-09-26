from src.models.client import Client
from src.schemes.client import ClientCreate, ClientFromDB, ClientFromFilter
from sqlalchemy import select, delete
from pydantic import UUID4


class ClientService:
    @staticmethod
    async def create(body: ClientCreate, db_session) -> ClientFromDB:
        query = Client(**body.model_dump(exclude_unset=True))
        db_session.add(query)
        await db_session.commit()
        await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def update(body: ClientFromDB, db_session) -> ClientFromDB:
        query = await db_session.execute(select(Client).where(Client.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query.serialize()

    @staticmethod
    async def filter(filters: ClientFromFilter, db_session) -> list[ClientFromDB]:
        query = select(Client)

        if filters.first_name is not None:
            query = query.where(Client.first_name.ilike(f'%{filters.first_name}%'))
        if filters.last_name is not None:
            query = query.where(Client.last_name.ilike(f'%{filters.last_name}%'))
        if filters.email is not None:
            query = query.where(Client.email.ilike(f'%{filters.email}%'))
        if filters.phone_number is not None:
            query = query.where(Client.phone_number.ilike(f'%{filters.phone_number}%'))

        query = query.limit(filters.limit).offset(filters.offset)

        result = await db_session.execute(query)
        clients = result.scalars().all()
        return [client.serialize() for client in clients]

    @staticmethod
    async def delete(uid: UUID4, db_session):
        stmt = delete(Client).where(Client.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

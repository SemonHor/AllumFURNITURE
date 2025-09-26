from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4

from src.schemes.client import ClientCreate, ClientFromDB, ClientFromFilter
from src.servises.client import ClientService


router = APIRouter()


@router.post("/create")
async def create(body: ClientCreate, db_session: AsyncSession = Depends(get_session)) -> ClientFromDB:
    return await ClientService.create(body, db_session)


@router.put("/update")
async def update(body: ClientFromDB, db_session: AsyncSession = Depends(get_session)):
    return await ClientService.update(body, db_session)


@router.get("/filter")
async def filter(body: ClientFromFilter = Query(...),
                 db_session: AsyncSession = Depends(get_session)) -> list[ClientFromDB]:
    return await ClientService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await ClientService.delete(uid, db_session)

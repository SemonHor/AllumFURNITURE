from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4


from src.schemes.furniture import FurnitureCreate, FurnitureFromDB, FurnitureFromFilter
from src.servises.furniture import create, update, \
    filter, delete_f


router = APIRouter()


@router.post("/create")
async def _create(body: FurnitureCreate, db_session: AsyncSession = Depends(get_session)):
    return await create(body, db_session)


@router.put("/update")
async def _update(body: FurnitureFromDB, db_session: AsyncSession = Depends(get_session)):
    return await update(body, db_session)


@router.put("/filter")
async def _filter(body: FurnitureFromFilter, db_session: AsyncSession = Depends(get_session)):
    return await filter(body, db_session)


@router.delete("/delete")
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await delete_f(uid, db_session)

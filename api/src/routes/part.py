from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4


from src.schemes.part import PartCreate, PartFromDB, PartFromFilter
from src.servises.part import PartService


router = APIRouter()


@router.post("/create")
async def create(body: PartCreate, db_session: AsyncSession = Depends(get_session)):
    return await PartService.create(body, db_session)


@router.put("/update")
async def update(body: PartFromDB, db_session: AsyncSession = Depends(get_session)):
    return await PartService.update(body, db_session)


@router.put("/filter")
async def filter(body: PartFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await PartService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await PartService.delete(uid, db_session)

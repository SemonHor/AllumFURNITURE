from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4

from src.schemes.partpreform import PartPreformCreate, PartPreformFromDB, PartPreformFromFilter
from src.servises.partpreform import PartPreform


router = APIRouter()


@router.post("/create")
async def create(body: PartPreformCreate, db_session: AsyncSession = Depends(get_session)):
    return await PartPreform.create(body, db_session)


@router.put("/update")
async def update(body: PartPreformFromDB, db_session: AsyncSession = Depends(get_session)):
    return await PartPreform.update(body, db_session)


@router.put("/filter")
async def filter(body: PartPreformFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await PartPreform.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await PartPreform.delete(uid, db_session)

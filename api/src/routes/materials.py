from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4

from src.schemes.materials import MaterialCreate, MaterialFromDB, MaterialFromFilter
from src.servises.material import MatherialService


router = APIRouter()


@router.post("/create")
async def create(body: MaterialCreate, db_session: AsyncSession = Depends(get_session)):
    return await MatherialService.create(body, db_session)


@router.put("/update")
async def update(body: MaterialFromDB, db_session: AsyncSession = Depends(get_session)):
    return await MatherialService.update(body, db_session)


@router.put("/filter")
async def filter(body: MaterialFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await MatherialService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await MatherialService.delete(uid, db_session)

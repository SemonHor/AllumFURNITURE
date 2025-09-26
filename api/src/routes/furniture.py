from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4


from src.schemes.furniture import FurnitureCreate, FurnitureFromDB, FurnitureFromFilter
from src.servises.furniture import FurnitureService


router = APIRouter()


@router.post("/create")
async def create(body: FurnitureCreate, db_session: AsyncSession = Depends(get_session)):
    return await FurnitureService.create(body, db_session)


@router.put("/update")
async def update(body: FurnitureFromDB, db_session: AsyncSession = Depends(get_session)):
    return await FurnitureService.update(body, db_session)


@router.put("/filter")
async def filter(body: FurnitureFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await FurnitureService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await FurnitureService.delete(uid, db_session)

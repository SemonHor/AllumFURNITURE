from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4


from src.schemes.bundle import BundleCreate, BundleFromDB, BundleFromFilter
from src.servises.bundle import BundleService


router = APIRouter()


@router.post("/create")
async def create(body: BundleCreate, db_session: AsyncSession = Depends(get_session)):
    return await BundleService.create(body, db_session)


@router.put("/update")
async def update(body: BundleFromDB, db_session: AsyncSession = Depends(get_session)):
    return await BundleService.update(body, db_session)


@router.put("/filter")
async def filter(body: BundleFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await BundleService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await BundleService.delete(uid, db_session)

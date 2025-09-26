from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4

from src.schemes.modificators import ModificatorCreate, ModificatorFromDB, ModificatorFromFilter
from src.servises.modificators import ModificatorService


router = APIRouter()


@router.post("/create")
async def create(body: ModificatorCreate, db_session: AsyncSession = Depends(get_session)):
    return await ModificatorService.create(body, db_session)


@router.put("/update")
async def update(body: ModificatorFromDB, db_session: AsyncSession = Depends(get_session)):
    return await ModificatorService.update(body, db_session)


@router.put("/filter")
async def filter(body: ModificatorFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await ModificatorService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await ModificatorService.delete(uid, db_session)

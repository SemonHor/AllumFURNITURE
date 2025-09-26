from fastapi.routing import APIRouter
from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from pydantic import UUID4

from src.schemes.order import OrderCreate, OrderFromDB, OrderFromFilter
from src.servises.order import OrderService


router = APIRouter()


@router.post("/create")
async def create(body: OrderCreate, db_session: AsyncSession = Depends(get_session)):
    return await OrderService.create(body, db_session)


@router.put("/update")
async def update(body: OrderFromDB, db_session: AsyncSession = Depends(get_session)):
    return await OrderService.update(body, db_session)


@router.put("/filter")
async def filter(body: OrderFromFilter = Query(...), db_session: AsyncSession = Depends(get_session)):
    return await OrderService.filter(body, db_session)


@router.delete("/delete")
async def delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await OrderService.delete(uid, db_session)

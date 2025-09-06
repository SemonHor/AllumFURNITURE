from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings

from src.schemes.furniture import FurnitureCreate, FurnitureFromDB
from src.schemes.part import PartCreate, PartFromDB

from src.servises.furniture import create_furniture, update_furniture
from src.servises.part import create_part, update_part

from src.db import get_session


router = APIRouter(prefix=settings.BASE_ROUTE_PATH)


# Создание и обновление мебели
@router.post("/create/furniture")
async def _create_furniture(body: FurnitureCreate, db_session: AsyncSession = Depends(get_session)):
    return await create_furniture(body, db_session)


@router.put("/update/furniture")
async def _update_furniture(body: FurnitureFromDB, db_session: AsyncSession = Depends(get_session)):
    return await update_furniture(body, db_session)


# Создание и обновление части мебели
@router.post("/create/part")
async def _create_part(body: PartCreate, db_session: AsyncSession = Depends(get_session)):
    return await create_part(body, db_session)


@router.put("/update/part")
async def _update_part(body: PartFromDB, db_session: AsyncSession = Depends(get_session)):
    return await update_part(body, db_session)


# @router.post("/create_furniture/{name}")
# async def add_furniture(name: str, db_session: AsyncSession = Depends(get_session)):
#     return await create_furniture(name, db_session)


# @router.post("/create_part/")
# async def add_part(body: dict, db_session: AsyncSession = Depends(get_session)):
#     return await create_part(body, db_session)


# @router.post("/set_bundle")
# async def add_bundle(body: BundleCreate, db_session: AsyncSession = Depends(get_session)) -> BundleFromDB:
#     return await create_bundle(body, db_session)


# @router.get("/get_stndr_bundle")
# async def get_stn_bundle(db_session: AsyncSession = Depends(get_session)) -> list[BundleFromDB]:
#     return await get_standart_bundles(db_session)

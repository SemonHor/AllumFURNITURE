from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.servises import create_furniture, create_part, find_standart_bundles,create_bundle
from src.schemes.bundle import BundleCreate,BundleFromDB
from src.db import get_session


router = APIRouter(prefix=settings.BASE_ROUTE_PATH)


@router.post("/create_furniture/{name}")
async def add_furniture(name: str, db_session: AsyncSession = Depends(get_session)):
    return await create_furniture(name, db_session)


@router.post("/create_part/")
async def add_part(body: dict, db_session: AsyncSession = Depends(get_session)):
    return await create_part(body, db_session)

@router.post("/set_bundle")
async def add_bundle(body: BundleCreate, db_session: AsyncSession = Depends(get_session)) -> BundleFromDB:
    return await create_bundle(body, db_session)

@router.get("/get_stndr_bundle")
async def get_stn_bundle(db_session: AsyncSession = Depends(get_session)) -> list[BundleFromDB]:
    return await find_standart_bundles(db_session)
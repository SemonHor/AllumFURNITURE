# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models.part import Part, Metarial, PartPreform
from src.models.furniture import Furniture
# from src.models.client import Client
from src.models.order import Bundle
from src.schemes.bundle import BundleCreate


async def name_in_parts(name: str, db_session):
    query = await db_session.execute(select(Part).filter_by(name=name))
    print(query)
    return query.scalars().first()


async def get_standart_bundles(db_session):
    query = await db_session.execute(select(Bundle).filter_by(is_standart=True))
    print(query)
    return query.scalars().all()


async def create_furniture(name: str, db_session):
    furniture = Furniture(name=name)
    db_session.add(furniture)
    await db_session.commit()
    return furniture


async def create_bundle(body: BundleCreate, db_session):
    bundle = Bundle(**body.model_dump(exclude_unset=True))
    db_session.add(bundle)
    await db_session.commit()
    return bundle.serialize()


async def create_part(body: dict, db_session):
    part = Part(furniture_uid=body['furniture_uid'])
    db_session.add(part)
    await db_session.commit()
    return part


async def create_material(body: dict, db_session):
    material = Metarial(name=body['name'], description=body['description'], uid_part=body['uid_part'])
    db_session.add(material)
    await db_session.commit()
    return material


async def create_part_preform(body: dict, db_session):
    part_preform = PartPreform(name=body['name'], description=body['description'], uid_part=body['uid_part'])
    db_session.add(part_preform)
    await db_session.commit()
    return part_preform

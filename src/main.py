import uvicorn
from fastapi import FastAPI

from src.routes.client import router as client_router
from src.routes.order import router as order_router
from src.routes.bundle import router as bundle_router
from src.routes.furniture import router as furniture_router
from src.routes.part import router as part_router
from src.routes.materials import router as materials_router
from src.routes.modifitors import router as modif_router
from src.routes.partpreform import router as part_pref_router

from src.config import settings
from fastapi.routing import APIRouter


app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(client_router, prefix='/client', tags=['Client'])
router.include_router(order_router, prefix='/order', tags=['Order'])
router.include_router(bundle_router, prefix='/bundle', tags=['Bundle'])
router.include_router(furniture_router, prefix='/furniture', tags=['Furniture'])
router.include_router(part_router, prefix='/part', tags=['Part'])
router.include_router(materials_router, prefix='/materials', tags=['Materials'])
router.include_router(modif_router, prefix='/modificator', tags=['Modificator'])
router.include_router(part_pref_router, prefix='/part_preform', tags=['PartPreform'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

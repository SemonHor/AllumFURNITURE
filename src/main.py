import uvicorn
from fastapi import FastAPI
from routes import router as rout
from config import BASE_ROUTE_PATH
from fastapi.routing import APIRouter


app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=BASE_ROUTE_PATH)

router.include_router(rout, prefix='/Furniture', tags=['Furniture'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

BASE_ROUTE_PATH = "/api"

app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=BASE_ROUTE_PATH)

@router.get("/hi")
async def get_hi():
    return "hi"

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

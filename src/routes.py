from fastapi.routing import APIRouter
from src.config import settings
from src.modules import orderFurnitureCost,findIdInAllStandartFurniture,furnitureCostCalc
from src.schemes import FurnitureInputScheme

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)


@router.put("/order_calc")
def giveFurnitureCost(ord: list[FurnitureInputScheme]):
    return orderFurnitureCost(ord)

@router.put("/furniture_calc")
def giveFurnitureCost(furniture: FurnitureInputScheme):
    return furnitureCostCalc(furniture)

@router.get("/standart_furniture/{ID}")
def findIdFurnitureCost(ID: int):
    return findIdInAllStandartFurniture(ID)
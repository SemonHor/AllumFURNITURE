from fastapi.routing import APIRouter
from src.config import settings
from src.modules import ORDER

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)


@router.put("/furniture_calc")
def give_furniture_cost(Furniture:dict):
    cost = 0
    for part in Furniture:
        cost+=(Furniture[part]['Cost'])
    return f'Итого:{int(cost)}'

@router.get("/standart_furniture/{ID}")
async def Find_id_furniture_cost_and_(ID):
    Md = {
        'Name':'Err404',
        'Cost':''
    }
    for Last_id in ORDER:
        if Last_id['id'] == ID:
            Md['Name'] = Last_id['Name']
            Md['Cost'] = give_furniture_cost(Last_id['Parts'])
    return Md
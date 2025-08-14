from fastapi.routing import APIRouter
from config import BASE_ROUTE_PATH
from modules import PARTS_ID_COST, MATHERIAL_EXTRA_CHARGE, EXTRA_CHARGE, ALL_FURNITURE


router = APIRouter(prefix=BASE_ROUTE_PATH)


@router.get("/furniture_calc/{Name_Type}/{List_Of_Parts}")
async def give_furniture_cost(Name_Type: str,List_Of_Parts,_Production_Cost=1.13):
    cost = 0
    if type(List_Of_Parts) is str:
        List_Of_Parts = List_Of_Parts.split('_')
    if List_Of_Parts == []:
        return 'Error404'
    for pr in List_Of_Parts:
        Count = pr[:pr.find('i')]
        Id=PARTS_ID_COST[pr[pr.find('d')+1:pr.find('M')]]
        MEC=MATHERIAL_EXTRA_CHARGE[pr[pr.find('M')+1:pr.find('H')]]
        H=pr[pr.find('H')+1:pr.find('W')]
        W=pr[pr.find('W')+1:]
        cost+=float(Count)*float(H)*float(W)*float(MEC)*float(Id)
    cost*=float(_Production_Cost)*float(EXTRA_CHARGE[Name_Type])
    return str(int(cost))


@router.get("/standart_furniture/{ID}")
async def Find_id_furniture_cost_and_(ID):
    Md = {
        'Name':'Err404',
        'Description':'',
        'Cost':''
    }
    for Last_id in ALL_FURNITURE:
        if Last_id['id'] == ID:
            Md['Name'] = Last_id['Name']
            Md['Description'] = Last_id['Description']
            Md['Cost'] = give_furniture_cost(Last_id['_Name_Type'],Last_id['_Parts'],Last_id['_production_cost'])
    return Md

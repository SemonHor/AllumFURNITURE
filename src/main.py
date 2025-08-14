import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

BASE_ROUTE_PATH = "/api/V1"

#Наценка.
EXTRA_CHARGE = {
    'standart':1,
    'dresser':2,
    'bedside':1.5,
    'сhair':3
}
#Цены за кв.см
_PARTS_ID_COST = {
    '1':10,
    '2':8,
    '3':7,
    '4':20,
    '5':7
}
_MATHERIAL_EXTRA_CHARGE = {
    '1':1,
    '2':1.5,
    '3':1.2,
    '4':2
}
#H и W - ширина и высота, измеряются в см; T - толщина, измеряется в мм
ALL_FURNITURE = [
    {
        'id':'0',
        'Name':'Шкаф <<Аполлон>>',
        'Description':'Суперсовременный шкаф состоящий из двух мебельных щитов и 4-х полок',
        '_Name_Type':'dresser',
        '_production_cost':'1.5',
        '_Parts':[
            '2id1M1H220W50',
            '4id2M1H50W50'
        ]
    },
    {
        'id':'1',
        'Name':'Прикроватная тумба <<Айда-баран>>',
        'Description':'Обычная тумбочка с чем-то',
        '_Name_Type': 'bedside',
        '_production_cost':'1.3',
        '_Parts':[
            '2id1M1H100W40',
            '2id2M1H50W30',
            '1id3M2H70W35'
        ]
    },
    {
        'id':'2',
        'Name':'Стул <<Вай>>',
        'Description':'Ну стул и стул',
        '_Name_Type': 'сhair',
        '_production_cost':'2',
        '_Parts':[
            '1id4M3H100W40',
            '1id5M4H50W50'
        ]
    }
]

app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

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
        Id=_PARTS_ID_COST[pr[pr.find('d')+1:pr.find('M')]]
        MEC=_MATHERIAL_EXTRA_CHARGE[pr[pr.find('M')+1:pr.find('H')]]
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

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

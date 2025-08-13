import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

BASE_ROUTE_PATH = "/api/V1"

#Наценка.
EXTRA_CHARGE = {
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
        'id':0,
        'Name':'Шкаф <<Аполлон>>',
        'Description':'Суперсовременный шкаф состоящий из двух мебельных щитов и 4-х полок',
        '_Name_Type':'dresser',
        '_production_cost':'1.5',
        '_Parts':[
            '2:id=1:M=1:[H:W]=[220:50]',
            '4:id=2:M=1:[H:W]=[50:50]'
        ]
    },
    {
        'id':1,
        'Name':'Прикроватная тумба <<Айда-баран>>',
        'Description':'Обычная тумбочка с ',
        '_Name_Type': 'bedside',
        '_production_cost':'1.3',
        '_Parts':[
            '2:id=1:M=1:[H:W]=[100:40]',
            '2:id=2:M=1:[H:W]=[50:30]',
            '1:id=3:M=2:[H:W]=[70:35]'
        ]
    },
    {
        'id':2,
        'Name':'Стул <<Вай>>',
        'Description':'',
        '_Name_Type': 'сhair',
        '_production_cost':'2',
        '_Parts':[
            '1:id=4:M=3:[H:W]=[100:40]',
            '1:id=5:M=4:[H:W]=[50:50]',
        ]
    }
]

app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=BASE_ROUTE_PATH)

@router.get("/furniture_calc/{Name_Type}?*{List_Of_Parts}*")
async def give_furniture_cost(Name_Type,List_Of_Parts,_Production_Cost=1.13):
    cost = 0
    if List_Of_Parts == []:
        return 'Error404'
    for part in List_Of_Parts:
        pos=part[part.rfind('[')+1:-1]
        cost+= part[part.find(':')]*_PARTS_ID_COST[part[part.find('=')+1]]*int(pos[:pos.find(':')])*int(pos[pos.find(':'):])
    cost*=_Production_Cost*EXTRA_CHARGE[Name_Type]
    return f"Итоговая стоимость: {cost} у.е."
# 1:id-3:M-2:[H:W]-[70:35]
@router.get("/standart_furniture/{ID}")
async def Find_id_furniture_cost(ID):
    for Last_id in ALL_FURNITURE:
        if Last_id[id] == ID:
            return give_furniture_cost(Last_id[_Name_Type],Last_id[_Parts],Last_id[_production_cost])
    return 'Error404'

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

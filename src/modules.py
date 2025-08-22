from src.schemes import FurnitureInputScheme,FurniturePartScheme


def furnitureCostCalc(furniture: FurnitureInputScheme):
    cost = 0
    print(furniture.parts)
    for part in furniture.parts:
       cost+=(part.cost)
    return cost

def findIdInAllStandartFurniture(ID: int):
    Md={'Name':'Err404','Cost':''}
    for Last_id in SF:
        if Last_id.furniture_id == ID:
           Md['Name'] = Last_id.furniture_name
           Md['Cost'] = furnitureCostCalc(Last_id)
    return Md

def orderFurnitureCost(ord: list[FurnitureInputScheme]):
    sumr = 0 
    for i in ord:
        sumr+=furnitureCostCalc(i)
    return sumr


SF =[FurnitureInputScheme(furniture_name="Шкаф",furniture_id=0,parts=[
                          FurniturePartScheme(part_name="Стойка",part_id=0,cost=7000,modificators={"P": 0,"O": 0,"P": 0}),
                          FurniturePartScheme(part_name="Стойка2",part_id=2,cost=9000,modificators={"P": 0,"O": 0,"P": 0})]),
    FurnitureInputScheme(furniture_name="Стул",furniture_id=1,parts=[
                          FurniturePartScheme(part_name="Стойка3",part_id=3,cost=100,modificators={"P": 0,"O": 0,"P": 0}),
                          FurniturePartScheme(part_name="Стойка4",part_id=4,cost=900,modificators={"P": 0,"O": 0,"P": 0})])]
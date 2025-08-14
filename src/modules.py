EXTRA_CHARGE = {
    'standart':1,
    'dresser':2,
    'bedside':1.5,
    'сhair':3
}
#Цены за кв.см
PARTS_ID_COST = {
    '1':10,
    '2':8,
    '3':7,
    '4':20,
    '5':7
}
MATHERIAL_EXTRA_CHARGE = {
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

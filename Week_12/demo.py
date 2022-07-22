G = [{
    'TID': 'Gurunath_8528',
    'Items': [
        {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
        {'Name': 'Pencil', 'Price': 10, 'Qty': 1},
        {'Name': 'Eraser', 'Price': 15, 'Qty': 1},
        {'Name': 'File', 'Price': 80, 'Qty': 1}
    ]
},
    {'TID': 'Max',
     'Items': [
         {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
         {'Name': 'Pencil', 'Price': 10, 'Qty': 1},
         {'Name': 'Eraser', 'Price': 15, 'Qty': 1},
         {'Name': 'File', 'Price': 90, 'Qty': 1}
     ]
     }

]

L = []

for x in G:
    D = {'ID': x['TID']}
    #print(x['TID'])
    val = 0
    for y in x['Items']:
        val += (y['Price'] * y['Qty'])
    D['Cost'] = val
    L.append(D)
print(L)


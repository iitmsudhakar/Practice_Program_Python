L = [{'TID': 'Gurunath_8528',
      'Items': [{'Name': 'Notebook', 'Price': 50, 'Qty': 4}, {'Name': 'Pencil', 'Price': 10, 'Qty': 1},
                {'Name': 'Eraser', 'Price': 15, 'Qty': 1},
                {'Name': 'File', 'Price': 80, 'Qty': 1}]}]

print(L[0])
print(L[0]['Items'])


def get_summary(trans):
    L = []
    for x in L:
        D = {'TID': x['TID']}
        val = 0
        for y in x['Item']:
            val = val + y['Price'] * y['Qty']
        D['Cost'] = val
        L.append(D)

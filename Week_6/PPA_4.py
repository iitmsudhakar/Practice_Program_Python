def value_to_keys(D, value):
    L=[]
    for key in D:
        if D[key] == value:
            L.append(key)
    return L



print(value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10))
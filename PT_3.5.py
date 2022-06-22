def _list(a,b):
    L = []
    new_L=[]
    for i in a:
        L.append(i)
    for j in b:
        L.append(j)
    while len(L) > 0:
        max = L[0]
        for x in L:
            if max > x:
                max = x
        new_L.append(max)
        L.remove(max)

    str = ''
    for x in new_L:
        str += x
    return str
  

a = input()
b = input()

print(_list(a,b))
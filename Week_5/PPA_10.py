def insert(L, x):
    L.append(x)
    print(L)
    new_list=[]
    while(len(L) > 0):
        max = L[0]
        for i in range(len(L)):
            if max > L[i]:
                max = L[i]
               
        new_list.append(max)
        L.remove(max)
    return new_list




print(insert([1,2,3,5],4))
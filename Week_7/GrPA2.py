
def merge(D1, D2, priority): 
    if priority=='first': 
        for i in D2: 
            print(i)
            if i not in D1: 
                D1[i]=D2[i] 
                print(D1[i])
        return D1 
    if priority=='second': 
        for i in D1: 
            print(i)
            if i not in D2: 
                D2[i]=D1[i] 
                print(D2[i])
        return D2


print(merge({1: 2, 2: 3, 3: 4},{1: 10, 4: 15, 5:10},'first'))
def uniq(L): 
    if len(L) == 1: 
        return L 
    if L[0] in L[1: ]: 
        return uniq(L[1: ]) 
    else: 
        return [L[0]] + uniq(L[1: ]) 



L = [1, 10, 1, 1000]

print(uniq(L))
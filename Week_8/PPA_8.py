def non_decreasing(L): 
    if len(L) <= 1: 
        return True 
    if L[0] > L[1]: 
        return False 
    return non_decreasing(L[1:]) 

L = [1, 10, 1, 1000]

print(non_decreasing(L))
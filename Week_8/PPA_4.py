def logarithm(x): 
    if x == 1: 
        return 0 
    else:
        return 1 + logarithm(x // 2) 

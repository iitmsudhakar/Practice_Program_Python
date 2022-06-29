def ancestry(P, present, past): 
    if present==past: 
        return [past] 
    else: 
        return ([present]+ancestry(P,P[present],past)) 

def steps(n): 
    if n==1 or n==0: 
        return 1 
    if n==2: 
        return 2 
    else: 
        return (steps(n-1)+steps(n-2)+steps(n-3)) 
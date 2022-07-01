def spiral_iterative(left, right, n): 
    for i in range(n - 1): 
        left, right = right, (left + right) / 2 
    return right 



def spiral_recursive(left, right, n): 
    if n == 1: 
        return right 
    return spiral_recursive(right, (left + right) / 2, n - 1) 

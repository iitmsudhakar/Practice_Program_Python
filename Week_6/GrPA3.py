def rotate(mat): 
    rotated=[] 
    for i in range(len(mat[0])): 
        turned=[] 
        for j in mat[::-1]: 
            turned.append(j[i]) 
        rotated.append(turned) 
    return rotated 
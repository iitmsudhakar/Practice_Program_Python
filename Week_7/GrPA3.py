def minor_matrix(M, i, j):
    len1 = len(M)
    len2 = len(M[0])
    temp = []
    for j in range(len1):
        if j == i:
            for k in range(len2):
                M.pop(M[i][k])
    for l in ran



def minor_matrix(M, i, j): 
    l=[] 
    for a in range(len(M)): 
        t=[] 
        if a==i: 
            continue 
        else: 
            for b in range(len(M[0])): 
                if b==j: 
                    continue 
                else: 
                    t.append(M[a][b]) 
    l.append(t) 
    return l 
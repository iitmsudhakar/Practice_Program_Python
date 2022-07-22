def matrix_type(M):
    dim = len(M)
    L = []
    for i in range(dim):
        for j in range(dim):
            if (i != j) and M[i][j] != 0 :
                return "non-diagonal"
            else:
                L.append(M[i][j])
               
    if len(set(L))== 2:
        if L[0] == 1:
            return "identity"
        else:
            return "scalar"
    else:
        return "diagonal"

L = []
for i in range(5):
    n = input()
    L.append(n)

sum = 0
for i in range(5):
    sum += int(L[i])
print(sum)
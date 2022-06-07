def get_column(mat, col):
    dim = len(mat)
    L = []
    for i in range(dim):
        L.append(mat[i][col])
    return L



def get_row(mat, row):
    dim = len(mat[0])
    L = []
    for i in range(dim):
        L.append(mat[row][i])
    return L

print(get_row([[1, 2], [3, 4]], 0))
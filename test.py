
import re


X = [[12,7,1],
    [4 ,5,1],
    [3 ,8,1]]


Y = [[12,7,2],
    [4 ,5,2],
    [3 ,8,2]]

dim1 = int(len(X))
dim2 = int(len(X[0]))
dim3 = int(len(Y))
dim4 = int(len(Y[0]))

result = []
added_mat = []

for i in range(dim2):
    result.append([])
for j in range(dim2):
    for k in range(dim1):
        result[j].append(0)

for i in range(dim2):
    added_mat.append([])
for j in range(dim2):
    for k in range(dim1):
        added_mat[j].append(0)

for i in range(dim2):2
    for j in range(dim1):
        result[i][j] = X[j][i]
'''
for i in range(dim1):
    for j in range(dim1):
        added_mat[i][j] = X[i][j] + Y[i][j]
'''

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            added_mat += X[i][k] * Y[k][j] 




print(result)
print(added_mat)



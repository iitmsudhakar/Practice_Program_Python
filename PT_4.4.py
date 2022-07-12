import numpy as np

n = int(input())
m = int(input())
A = []
for i in range(n):
    A.append(input().split(','))
    for j in range(n):
        A[-1][j] = int(A[-1][j])

print(A)

A = np.matrix(A)
C = A*A*A

print(C)
#print(A)

B = []
for i in range(len(A)):
    B.append([])
for i in range(len(A)):
    for j in range(len(A[0])):
        B[i].append(0)

print(B)
for i in range(m):
    for p in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A)):
                B[i][j] += A[i][k] * A[k][j]
print(B)

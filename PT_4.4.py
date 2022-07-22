n = int(input())
m = int(input())
A = []
for i in range(n):
    A.append(input().split(','))
    for j in range(n):
        A[-1][j] = int(A[-1][j])

B = A
for x in range(m - 1):
    t = []
    for i in range(n):
        y = []
        for j in range(n):
            c = 0
for k in range(n):
    c += A[i][k] * B[k][j]
    y.append(c)
    t.append(y)
B = t
print(B)

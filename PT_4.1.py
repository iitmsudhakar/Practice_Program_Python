n = int(input())
A=[]
for i in range(n):
    A.append(input().split(','))
    for j in range(2):
        A[-1][j] = int(A[-1][j])

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    if gcd(x, y) == 1:
        return 'YES'
    else:
        return 'NO'

L = []
for k in range(len(A)):
    for l in range(1):
        x = A[k][l]
        y = A[k][-1]
        L.append(is_coprime(x,y))

delim = ','
s = delim.join(L)

print(L)








        
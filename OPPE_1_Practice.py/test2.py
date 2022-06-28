L = [1,1,2,3,4,5,6,6,2,3,3,2,9,5,5,3,6,1,3,7,9,4]
'''
S = set(L)
D ={}
for i in S:
    D[i] = 0
NL = []

for i in L:
    D[i] += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


G = (D.keys())

print(G)
print(D)
O = []
for i in D:
    for j in range(D[i]):
        U = D.keys()

print(U)

'''
NL = [] 
SL = []   
for i in range(len(L)):
    for j in range(1,len(L)):
        if L[i] == L[j]:
            SL.append(L[i])
        NL.append(SL)

print(NL)


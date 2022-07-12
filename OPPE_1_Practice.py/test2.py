from itertools import groupby

L = [11, 3, 11, 3, 7, 7, 6, 5, 5, 7, 6, 6, 2, 1]

L.sort()

print([list(j) for i, j in groupby(L)])
NL = []
SNL = []
while len(L) > 0:
    for i in range(len(L)):
        if L[i] != L[i+1]:
            NL.append(L[i])
            SNL.append(NL)
            L.remove(L[i])
            print(SNL)
        if L[i] == L[i+1]:
            NL.append(L[i])
            NL.append(L[i+1])
            SNL.remove(L[i])
            SNL.remove((L[i+1]))
            L.remove(L[i])
            L.remove(L[i+1])

print(SNL)


L = [[0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 1], [0, 0, 0, 1]]
RL = []
x = 0
for i in range(len(L[0])):
    TL = []
    for j in range(len(L)):
        x = L[j][i]
        TL.append(x)
    RL.append(TL)
print(RL)


def max(L):
    profit = 0
    max_profit = 0
    #while len(L) > 0:
    for i in range(len(L)):
        for j in range(1,len(L)):
            if L[i][1] != L[j][1] and L[i][2] != L[j][2]:
                if L[i][1] > L[j][1] and L[i][1] < L[i][2] and L[i][2]> L[i][1] and L[i][2] < L[j][2]:
                    if L[i][3] > L[j][3]:
                        profit = L[i][3]
                        max_profit += profit
                        #L.remove(L[0])
                    else:
                        profit = L[j][3]
                        max_profit += profit
                        #L.remove(L[0])
        
    return max_profit
    




L = [('A',1,2,40),('B',3,4,5),('C',0,7,6),('D',1,2,3),('E',5,6,8),('F',5,9,2),('G',10,11,9),('H',0,11,35)]

print(max(L))
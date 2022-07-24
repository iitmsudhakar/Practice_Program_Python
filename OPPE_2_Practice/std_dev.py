def _mean(L):
    sum = 0
    length = len(L)
    for i in range(len(L)):
        sum += L[i]
    mean = sum/length
    return mean

def summation(L):
    mean = _mean(L)
    summation = 0
    for i in range(len(L)):
        summation += (L[i] - mean)**2
    return summation

def _std_dev(L):
    num = summation(L)
    den = int(len(L))-1
    std_dev = (num/den) ** 0.5
    std_dev = (std_dev)
    return std_dev

def max_std(L):
    tem_L = []
    for i in range(len(L)):
        x = _std_dev(L[i])
        print(x)
        tem_L.append(x)
    max = 0
    ind= []
    for j in range(len(tem_L)):
        com = int(tem_L[j])
        if com >= max:
            max = com
            ind.append(j)
    last = ind[-1]
    return last



print(max_std([[10, 12, 23, 23, 16, 23, 21, 16],[4, 9, 11, 12, 17, 5, 8, 12, 14],[4.5, 9.7, 11, 12, 10, 5, 8, 12, 14]]))





total = 0.1*(100) + 0.1*(38)
T1 = (0.5 * 70) +(0.2 * 75) + 1.5
T2 = (0.4 * 70) + (0.3 * 75) + (0.1 * 55) + 1.5
#print(T1, T2)
#Ly = max[T1, T2]
total1 = total + T1
total2 = total + T2

print(total1, total2)

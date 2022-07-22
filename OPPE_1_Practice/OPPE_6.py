def optimal_cut(l, L):
    L.sort(reverse=True)
    sum = 0
    for i in range(2):
        sum  += L[i]
    return sum


#print(optimal_cut(3,[10, 20, 20, 5, 3]))

s = +5-2

print(type(s))
print(s)
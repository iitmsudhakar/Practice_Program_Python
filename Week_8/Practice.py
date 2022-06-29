def equality(P, Q):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] != Q[0]:
        return False
    return equality(P[:-1], Q[:-1])

P = [1,2,3,4,5,6,7,8,8,10]
Q = [1,2,3,4,4,6,7,8,9,10]

#print(equality(P,Q))

def bin_to_dec(bin):
    if len(bin) == 1:
        return int(bin)
    init = bin[:-1]
    last = bin[-1]
    return bin_to_dec(init) * 2 + last

print(bin_to_dec('101'))
print(bin_to_dec('0'))
print(bin_to_dec('1'))
print(bin_to_dec('101101'))
#print(bin_to_dec('101'))
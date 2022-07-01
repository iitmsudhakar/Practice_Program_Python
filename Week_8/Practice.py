def equality(P, Q):
    size = len(P)
    for i in range(size):
        if P[i] != Q[i]:
            return False
    return True

P = [1,2,3,4,5,6,7,8,9]
Q = [1,2,3,4,4,6,7,8,9,10]

print(equality(P,Q))

def bin_to_dec(bin):
    if len(bin) == 1:
        return int(bin)
    init = bin[:-1]
    last = bin[-1]
    return bin_to_dec(init) * 2 + last

#print(bin_to_dec('101'))
#print(bin_to_dec('0'))
#print(bin_to_dec('1'))
#print(bin_to_dec('101101'))
#print(bin_to_dec('101'))
def equality(P, Q):
    if len(P) != len(Q):
        return False
    for elem in P:
        if elem not in Q:
            return False
    return True


P = [1,2,3,5,5,6,7,3,9,10]
Q = [1,2,3,4,5,6,7,8,9,10]

print(equality(P,Q))
def factors(n):
    S = set()
    for i in range(1,n + 1):
        if n % i == 0:
            S.add(i)
    return S


def common_factors(a, b):
    S1 = factors(a)
    S2 = factors(b)
    S = S1.intersection(S2)
    return S

def factors_upto(n):
    D = dict()
    for i in range(1,n + 1):
        D[i] = factors(i)
    return D



print(factors_upto(20))
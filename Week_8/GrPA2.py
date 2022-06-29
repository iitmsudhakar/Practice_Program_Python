def linear(P,Q,K):
    if len(P) != len(Q):
        return False
    if len(P)==0:
        return True
    if Q[0] * K != P[0]:
        print(Q[0] * K)
        print(P[0])
        return False
    return linear(P[1:],Q[1:],K)



P = [10, 20, 30, 40, 50]
Q = [1, 2, 3, 4, 6]
K = 10

print(linear(P,Q,K))
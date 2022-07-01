def search(L,K):
    if len(L) == 0:
        return False
    if L[0] == K:
        return True
    return search(L[1:],K)
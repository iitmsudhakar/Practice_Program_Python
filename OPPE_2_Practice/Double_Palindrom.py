n = int(input())


def _list(n):
    L = []
    for i in range(10, n + 1):
        L.append(i)
    return L


def _square(L):
    SL = []
    for i in L:
        x = i ** 2
        SL.append(x)
    return SL


def _palindrom(num):
    reverse = int(str(num)[::-1])
    if num == reverse:
        return True
    else:
        return False

L1 = _list(n)
L2 = _square(L1)


def _doublepalindrom(L1, L2):
    L3 = []
    for x, y in zip(L1, L2):

        if x >= 10 and y >= 10:
            if _palindrom(x) and _palindrom(y):
                L3.append(x)
                L3.append(y)
    return L3


print(_doublepalindrom(L1, L2))
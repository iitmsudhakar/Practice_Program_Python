def _mean(L):
    leng = len(L)
    sum = 0
    for x in L:
        sum += x
        mean = sum / leng
    return mean


def _sum(L):
    sum = 0
    for x in L:
        sum += x
    return sum


def _stddev(L):
    l = len(L) - 1
    NL = _calc1(L)
    sum = _sum(NL)
    st = sum / l
    std = (sum / l ) ** 0.5
    return std


def _calc1(L):
    NL = []
    m = _mean(L)
    for i in L:
        x = (i - m) ** 2
        NL.append(x)
    return NL


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(_stddev(L))

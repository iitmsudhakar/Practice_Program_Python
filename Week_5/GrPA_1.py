def _max(L):
    maximum = L[0]
    for x in L:
        if x > maximum:
            maximum = x
    return maximum
        
def _min(L):
    minimum = L[0]
    for x in L:
        if x < minimum:
            minimum = x
    return minimum


def get_range(L):
    maxi = _max(L)
    mini = _min(L)
    range = maxi - mini
    return range


print(get_range([1.0,2.0,3.0,4.0,5.0]))
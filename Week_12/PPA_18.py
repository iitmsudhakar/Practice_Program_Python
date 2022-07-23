def _keys(L):
    keys = []
    for i in range(len(L)):
        keys.append(i)
    return keys


def _value(L):
    value = []
    for i in range(len(L)):
        value.append(L[i])
    return value


def list_to_dict(L):
    key = _keys(L)
    value = _value(L)
    D = dict(zip(key, value))
    return D


print(list_to_dict([[1, 2, 3], [1, 2, 3]]))

def _keys1(D):
    keys = []
    for x in D:
        keys.append(x)
    return keys



def dict_to_list(D):
    value = []
    for x in D:
        y = D[x]
        value.append(y)
    return value

print(_keys1({0: [1, 2, 3], 1: [1, 2, 3]}))
print(dict_to_list({0: [1, 2, 3], 1: [1, 2, 3]}))
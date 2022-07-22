def val(x, y):
    value = 30 + x ** 2 + y ** 2 - 3 * x - 4 * y
    return value


def survival(T):
    for i in range(6):
        for j in range(6):
            if val(i, j) <= T:
                return True
    return False

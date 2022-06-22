def is_key(D, key):
    if key in D:
        return True
    else:
        return False


def value(D, key):
    if key in D:
        value = D[key]
        return value
    else:
        return None



print(is_key({'good': 4, 'day': 3}, 'day'))

print(value({'good': 4, 'day': 3}, 'good'))
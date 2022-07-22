


def exact_count(para, n):
    L = para.split(' ')
    for word in L:
        if L.count(word) == n:
            return True
    return False


print(exact_count('good word many good works good real choice',4))



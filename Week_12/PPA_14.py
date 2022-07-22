def crowded_group(scores, sub, mark_limit):
    L = [ ]
    for st in scores:
        L.append(st[sub])
    L.sort()
    gsize = 1
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] - L[i] <= mark_limit:
                if j - i + 1> gsize:
                    gsize = j - i + 1
    return gsize
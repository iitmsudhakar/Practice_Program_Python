def file_to_list(fname):
    f = open(fname, 'r')
    n = f.readline().strip().split(',')
    # print(n)

    L = []
    for line in f:
        d = {}
        ll = line.strip().split(',')
        # print(ll)
        for i in range(len(ll)):
            if n[i] != 'Name':
                val = int(ll[i])
            else:
                val = ll[i]
            d[n[i]] = val
        L.append(d)
    f.close()
    print(L)


print(file_to_list('scores.csv'))

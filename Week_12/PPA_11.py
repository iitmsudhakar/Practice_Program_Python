def file_to_dict(fname):
    f = open(fname, 'r')
    n = f.readline().strip().split(',')
    d = {}
    print(n)

    for i in n:
        d[i] = []
    print(d)

    dl = len(d)
    for line in f:
        nl = line.strip().split(',')
        for i in range(len(nl)):
            col_name = n[i]
            if col_name != 'Name':
                val = int(nl[i])
            else:
                val = nl[i]
            d[col_name].append(val)
        f.close()
        return d

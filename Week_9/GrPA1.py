def get_freq(filename):
    f = open(filename, 'r')
    d = {}
    for line in f:
        word = line.strip()
        if word not in d:
            d[word] = 0
        else:
            d[word] += 1
    f.close()
    return  d
def get_dict(filename):
    f = open(filename, 'r')
    # print(f)
    f.readline()
    # print(g)
    P = dict()
    for line in f:
        print(line)
        name, age = line.strip().split(',')
        #age = line.strip().split(',')
        #print(name, age)
        age = int(age)
        P[name] = age
    f.close()
    return P


path = "filename.txt"

print(get_dict(path))

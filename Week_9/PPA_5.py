def get_matrix(filename):
    f = open(filename, 'r')
    #print(f)
    M = []
    for line in f:
        print(line)
        row = line.split(',')
        print(row)
        for i in range(len(row)):
            print(i)
            row[i] = int(row[i])
            print(row)
        M.append(row)
    f.close()
    return M


path = "filename.txt"

print(get_matrix(path))
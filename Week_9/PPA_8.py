def improvement(filename):
    f = open(filename, "r")
    f.readline()
    lst = []
    for line in f:
        L = line.split(",")
        lst.append(L)
    count = 0
    for i in range(len(lst)):
        # for j in range(len(lst[i])):
        if lst[i][-1] > lst[i][-2] > lst[i][-3]:
            count += 1
    return count

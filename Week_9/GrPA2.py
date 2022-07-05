def relation(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    L1 = []
    L2 = []
    for line in f1:
        L = line.strip()
        L1.append(L)
    for line in f2:
        L = line.strip()
        L2.append(L)
    if int(len(L1)) < int(len(L2)):
        for i in range(len(L1)):
            if L1[i] == L2[i]:
                return "Subset"

    if L1 == L2 and int(len(L1)) == int(len(L2)):
        return "Equal"
    else:
        return "No Relation"


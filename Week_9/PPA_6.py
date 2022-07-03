def write_AP(a_1, d, n):
    a_1 = int(a_1)
    d = int(d)
    n = int(n)
    f = open("out.txt", "w")
    f.write(str(a_1)+'\n')
    for i in range(n-1):
        if i != n-1:
            a_1 += d
            f.write(str(a_1) + '\n')
        else:
            a_1 += d
            f.write(str(a_1))
        #print (a_1)


write_AP(1,3,5)
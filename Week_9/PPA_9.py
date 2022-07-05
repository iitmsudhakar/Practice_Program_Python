def extract_lines(filename):
    f = open(filename, "r")
    g = open("python.csv", "w")
    header = f.readline()
    g.write(header)
    for line in f:
        print(line)
        L = line.strip().split(",")
        print(L)
        py = int(L[4])
        gender = L[2]
        if gender == 'M' and py >= 70:
            g.write(line)
    f.close()
    g.close()


print(extract_lines('filename.txt'))

def add_period(filename):
    r = open(filename, 'r')
    w = open("out.txt", "w")
    for line in r:
        line = line.strip()
        w.write(line + '.' + '\n')
    r.close()
    w.close()

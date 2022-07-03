def read_file(filename):
    f = open(filename, 'r')
    line = f.readlines()
    for i in f:
        print(line.strip())
    f.close()


print(read_file('Practice_Program_Python\Week_9\files\words.txt'))
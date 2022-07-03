def get_max_line(filename): 
    f = open(filename, 'r') 
    line = f.readline() 
    maxnum, maxline = int(line.strip()), 1
    count = 1
    for line in f: 
        num = int(line.strip()) 
        count += 1
        if num > maxnum: 
            maxnum = num 
            maxline = count 
    f.close() 
    return maxline

file = "filename.txt"

print(get_max_line(file))
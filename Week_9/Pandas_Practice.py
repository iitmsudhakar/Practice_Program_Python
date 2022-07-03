import pandas as pd

path = 'Practice_Program_Python\Week_9\scores.csv'
data = pd.read_csv(path)

#print(data)
#print(data.count())

def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)
    
    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)
    
    f.close()
    g.close()
    
#do_something('Practice_Program_Python\Week_9\scores.csv', 'F', 'Practice_Program_Python\Week_9\out.csv')

def do_something(filename):
    f = open(filename, 'r')
    maxword = f.readline().strip()
    count = 1
    # we are now at the beginning of the second line
    for line in f:
        word = line.strip()
        if len(word) > len(maxword):
            maxword = word
            count = 1
        elif len(word) == len(maxword):
            count += 1
    
    f.close()
    return count

print(do_something('Practice_Program_Python\Week_9\words.txt'))
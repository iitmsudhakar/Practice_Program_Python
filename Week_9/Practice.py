def do_something(filename, sub):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    val, count = 0, 0
    
    for line in f:
        sno, name, gender, ct, python, pdsa = line.strip().split(',')
        sno, ct, python, pdsa = int(sno), int(ct), int(python), int(pdsa)
        if sub == 'CT':
            val = val + ct
        elif sub == 'Python':
            val = val + python
        elif sub == 'PDSA':
            val = val + pdsa
        count = count + 1
        
    f.close()
    return val / count


def get_scores(filename, index):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    
    scores = [ ]
    line = f.readline()
    while line != '':
        L = line.strip().split(',')
        scores.append(int(L[index]))
        line = f.readline()
    
    f.close()
    return scores


def do_something(L):
    L.sort()
    mid = len(L) // 2
    if len(L) % 2 == 0:
        return (L[mid] + L[mid - 1]) // 2
    else:
        return L[mid]


L = [90,80,100,100,70,95,65,75,85,95]

print(do_something(L))

# Hint: int(1.5) is 1
#print(int(do_something('Practice_Program_Python\Week_9\scores.csv', 'Python')))

#print(get_scores('Practice_Program_Python\Week_9\scores.csv','3'))
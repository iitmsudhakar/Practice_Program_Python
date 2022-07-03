
def get_dict(filename): 
    f = open(filename, 'r') 
    f.readline() 
    P = dict() 
    for line in f: 
        name, age = line.strip().split(',') 
        age = int(age) 
        P[name] = age 
    f.close() 
    return P


print(get_dict('filename.txt'))
def get_matrix(filename): 
    f = open(filename, 'r') 
    M = [ ] 
    for line in f: 
        row = line.split(',') 
        for i in range(len(row)): 
            row[i] = int(row[i]) 
        M.append(row) 
    f.close() 
    return M 

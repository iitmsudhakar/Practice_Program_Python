X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
 
Y = [[10,11,12],  
      [13,14,15],  
      [16,17,18]]  
 
result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  

added_mat = []

for i in range(len(X)):
    added_mat.append([])
for j in range(len(X)):
    for k in range(len(X)):
        added_mat[j].append(0)

print(added_mat)

'''
# iterate through rows of X  
for i in range(len(X)):  
   for j in range(len(Y[0])):  
       for k in range(len(Y)):  
           result[i][j] += X[i][k] * Y[k][j]  
'''

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j] 


print(result)

Z = [[10,11,12],[13,14,15],[16,17,18]]   
S = []
for i in range(len(Z)):
    max = Z[i][0]
    for j in range(len(Z[i])):
        if Z[i][j] > max: 
            max = Z[i][j]
    S.append(max)

for i in S:
    max = i
    if i > max:
        max = i
print(S)
print(max)
       
L = [1,1,3,3,4,5,6,7,4,5,7,2,3,7,9,2,3,8]

Q = set(L)
print(Q)
D = {}
for i in Q:
    D[i] = 0

for i in L:
    D[i] += L.count(i)




print(D)
max = D[i]
for i in D:
    if D[i] > max: 
        max = D[i]
        
print(max,i)

print(D.items())
print(D.keys())
print(D.values())
# functionprint(L.count(1))
      
      
 
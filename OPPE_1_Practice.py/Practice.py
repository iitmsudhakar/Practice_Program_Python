import random
from re import T

d = {}
'''
for i in range(10):
    d[i] = 0
'''
L = []
for i in range(20):
   k = random.randint(0,9)
   L.append(k)

print(L)
s = set(L)
print(s)
for j in s:
    d[j] = 0

print(d)

for l in L:
    d[l] += 1
'''
for i in range(len(d)):
    if d[i] == 0:
        del d[i]   
'''
print(d)
#print(len(d))

max = d[0]
value = 0
for i in d:
    if d[i] > max:
        #print(d[i])
        max = d[i]
        value = i
print(value,max)



'''
n = int(input())
station_dict = dict()

for i in range(n):
    train = input()
    coach = int(input())
    d = dict()
    for i in range(coach):
        compartment = input().split(',')
        d[compartment[0]] = int(compartment[1])
    station_dict[train[0]] = d
'''

#print(max[1,2,3,4,5])


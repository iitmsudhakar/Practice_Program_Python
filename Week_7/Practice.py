'''
n = int(input())
L = [ ]
for i in range(n):
    line = input().split(',')
    L.append(line)

print(L)
'''
from copyreg import pickle


L= [['eng2', 'eng1'], ['python', 'CT'], ['MFL', 'M2', 'M1']]

def prereq(L):
    D = dict()
    main = L[0]
    for course in L[1: ]:
        if main in D:
            D[main].append(course)
        else:
            D[main] = [course]
    return D

#print(prereq(L))

#{'eng2': ['eng1'], 'python': ['CT'], 'MFL': ['M2', 'M1']}

def get_basic(D):
    basic = [ ]
    for main in D:
        for course in D[main]:
            if course not in D:
                basic.append(course)
    return set(basic)


def pinnacle(D):
    S = set()
    for main_1 in D:
        flag = False
        for main_2 in D:
            if main_1 in D[main_2]:
                flag = True
                break
        if flag:
            S.add(main_1)
    return S

def get_deep(D):
    deep = [ ]
    maxpre = 1
    for main in D:
        if len(D[main]) > maxpre:
            maxpre = len(D[main])
            deep = [main]
        elif len(D[main]) == maxpre:
            deep.append(main)
    return deep


print(get_deep({'eng2': ['eng1','grammer'], 'python': ['CT','Java'], 'MFL': ['M2', 'M1'],'MFL2': ['M5', 'M4','M3']}))
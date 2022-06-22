# Dictionary #set #list

import re


def str_list(x):
    L = list(x.split(' '))
    return L


def _rem_punc(x):
    punc = '!()-[]{};:\'\"\,<>./?@#$%^&*_~'
    for ele in x:
        if ele in punc:
            x = x.replace(ele, "")
    return x




def li_se(L):
    s = set(L)
    return s

def _init_set(L):
    d ={}
    for x in li_se(L):
        d[x] = 0               
    return d

#print(_init_set(['hello','world','how','are','you','you']))

def _max_freq(L):
    y = str_list(_rem_punc(L))
    d = {}
    for x in li_se(y):
        d[x] = 0 
    max = 0
    ans = ''
    for x in y:
        d[x]= d[x]+1
        if d[x] > max: 
           max = d[x]
           ans = x
    return d


def _para(x):
    count = x.count('.')
    return count


print("Please enter the para")
para = input()

print(_max_freq(para))
print(_para(para))



#print(_max_freq('The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.'))









n = input()
L = n.split(' ')

numbers = {'zero':0,'one':1, 'two':2, 'three':3, 'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'plus': '+', 'minus': '-'}

M = []

for i in L:
    if i in numbers:
        M.append(numbers[i])
    print(M)

eval =''
for j in M:
    if j == "-":
        eval += ('-')
    elif j == '+':
        eval += ('+')
    else:
        eval += str(j)
s = int
for k in eval:
    s += int(k)



print(type(s))
print(s)





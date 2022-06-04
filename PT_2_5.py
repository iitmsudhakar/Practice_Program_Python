'''
Accept four integers as input and write a program to print these integers in non-decreasing order.

The input will be four integers in four lines. The output should be a single line with all the integers separated 
by a single space in non-decreasing order.

Note: There is no space after the fourth integer.


'''

# 4 integers as input and
L= []
for i in range(4):
    L.append(int(input()))

#print(L)

sort_list = []

#print(sort_list)

while len(L)>0:
    min = L[0]
    for i in range(len(L)):
        if min > L[i]:
            min = L[i]
    sort_list.append(min)
    L.remove(min)

#print(sort_list)

for elem in sort_list:
    print(elem,end=' ')

    


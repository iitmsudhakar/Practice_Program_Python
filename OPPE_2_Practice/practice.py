'''
Accept a ten-digit number as input. Find the number of places where the numbers 0 and 1 have been replaced by letters.
If there are no such replacements, print the string No mistakes.
If not, print the number of mistakes (replacements) and in the next line, print the correct phone number.
'''

'''
def _count(n):
    num_lst = []
    for x in n:
        num_lst.append(x)
        count = int(num_lst.count('l')) + int(num_lst.count('o'))
    return count


def _replace(n):
    num_lst = []
    for x in n:
        num_lst.append(x)
    for i in range(len(num_lst)):
        if num_lst[i] == 'l':
            num_lst[i] = '1'
        if num_lst[i] == 'o':
            num_lst[i] = '0'
    num_crt = ''
    for x in num_lst:
        num_crt = num_crt + x
    return num_crt


n = input()
if _count(n) == 0:
    print("No mistakes")
else:
    print(f'{_count(n)} mistakes')
    print(_replace(n))
'''

'''
Accept a sequence of comma-separated integers as input. Determine 
if the sequence is left-heavy, right-heavy or balanced and print this as the output.

'''

'''
num = input().split(',')


def sum(num):
    mid = int(len(num)) // 2
    L_sum = 0
    R_sum = 0
    for i in range(0, mid):
        L_sum += int(num[i])
    for i in range(-1, mid - 1):
        R_sum += int(num[i])
    if L_sum == R_sum:
        print("balanced")
    if L_sum > R_sum:
        print("left-heavy")
    if L_sum < R_sum:
        print("right-heavy")


sum(num)
'''
'''
diagonal: if the entries outside the main-diagonal are all zeros
scalar: if it is a diagonal matrix, all of diagonal elements are equal
identity: if it is a scalar matrix, all of whose diagonal elements are equal to 1
'''


def matrix_type(M):
    dim = len(M)
    L = []
    for i in range(dim):
        for j in range(dim):
            if i != j and M[i][j] != 0:
                return "non-diagonal"
            else:
                L.append(M[i][j])
    if len(set(L)) == 2:
        if L[0] == 1:
            return "identity"
        else:
            return "scalar"
    else:
        return "diagonal"



M = [[2, 0, 1], [0, 3, 0], [0, 0, 4]]

print(matrix_type(M))

'''
Two strings are said to be equivalent if either string can be obtained by rearranging the characters of the other
string. For example, good and odog are equivalent. But apple and lape are not equivalent.
Accept two strings as input. Print Equivalent if both the strings are equivalent and Not Equivalent otherwise.
'''


def _str_lst(S):
    L = []
    for i in S:
        L.append(i)
    return L


'''
def _check(L1, L2):
    for i in L1:
        if i in L2:
            return True
        else:
            return False
'''


def _check2(L1, L2):
    if len(L1) != len(L2):
        return False
    count = 0
    for i in L1:
        if L1.count(i) == L2.count(i):
            count += 1
        if count == len(L1):
            return True




str_1 = input().lower()
str_2 = input().lower()

# print(str_1, str_2)

L1 = _str_lst(str_1)
L2 = _str_lst(str_2)

if _check2(L1, L2):
    print("Equivalent")
else:
    print('Not Equivalent')

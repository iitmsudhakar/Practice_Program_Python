def is_empty(L):
    if len(L) == 0:
        return True
    else:
        return False

def first(L):
    if is_empty(L):
        return 'None'
    else:
        return  L[0]


def last(L):
    if is_empty(L):
        return 'None'
    else:
        return  L[-1]

def init(L):
    first_list = []
    if is_empty(L):
        return 'None'
    else:
        for i in range(len(L)-1):
            first_list.append(L[i])
        return first_list


def rest(L):
    rest_list = []
    if is_empty(L):
        return 'None'
    else:
        for i in range(1,len(L)):
            rest_list.append(L[i])
        return rest_list


def type_of_sequence(L):
    sum = 0
    mysterious = []
    for elem in L:
        if mysterious(elem):
            sum += 1
    if sum < 2 :
        return 'mildly mysterious'
    elif sum >=2 and sum < 5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'

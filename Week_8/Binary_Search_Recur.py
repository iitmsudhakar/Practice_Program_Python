def rec_binary_search(L,K,start,end):
    '''This function with recursivly compute the binary search'''
    # when start and end are same, we just check if start or end is equal to value
    if (start == end):
        if start == K:
            return "Value is present"
        else:
            return "Value is not present"
    # when start and end are consecutive then we check if value is equal to start or end
    if (end - start) == 1:
        if (L[start] == K) or (L[end] == K):
            return "Value is present"
        else:
            return "Value is not present"
    # when end - start is greater than 1 then we compute the mid point and compare it with value to check
    # which side to disgard

    if (end - start) > 1:
        mid = (start+end) // 2
        if L[mid] > K:
            end = mid - 1
        if L[mid] < K:
            start = mid + 1
        if L[mid] == K:
            return "Value is present"

    if end - start < 0:
        return "Value is not present"

    return rec_binary_search(L,K,start,end)


L = [1,2,3,4,5,6,7,8,9,300,500]

print(rec_binary_search(L,99,0,11))
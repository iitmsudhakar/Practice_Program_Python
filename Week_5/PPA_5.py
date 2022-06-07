def first_three(L):
    new_list=[]
    final_list = []
    while(len(L) > 0):
        max = L[0]
        for i in range(len(L)):
            if max < L[i]:
                max = L[i]
        new_list.append(max)
        print(new_list)
        L.remove(max)
    for i in range(3):
        final_list.append((new_list[i]))
    return final_list


print(first_three([1,2,3,4,5]))
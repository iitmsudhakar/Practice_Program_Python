import random

def binary_search(list,value):
    #finding the mid point of the list
    #begin point
    a = 0
    #end point
    b = len(list) - 1
    #mid point
    
    while (b-a >1):
        mid = (a + b) // 2
        if list[mid] == value:
            return "Value is present"       
        if list[mid] > value:
            b = mid - 1
        if list[mid] < value:
            a = mid + 1       
    if list[a] == value or list[b] == value:
        return "Value is present"
    else:
        return "Value is not present"





a_list = list(range(1, 101))
print("Enter a number from 1-100 to check if that is present in the list")
value = int(input())

print(binary_search(a_list,value))

import random


def binary_search(list, value):
    # finding the mid point of the list
    # begin point
    a = 0
    # end point
    b = len(list) - 1
    # mid point

    while b - a > 1:
        mid = (a + b) // 2
        if list[mid] == value:
            return "Great !! Your guess value is present"
        if list[mid] > value:
            b = mid - 1
        if list[mid] < value:
            a = mid + 1
    if list[a] == value or list[b] == value:
        return "Great !! Your guess value is present"

    else:
        return "Hmm No !! Value is not present"


a_list = []
for i in range(100):
    num = (random.randint(0, 99))
    a_list.append(num)

a_list = sorted(a_list)
# print(a_list)
# print(len(a_list))

print("Enter a number from 0-100 to check if that is present in the random list")
value = int(input())
print(binary_search(a_list, value))

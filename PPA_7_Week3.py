# Magical word 

str_1 = str(input())
str_2 = str(input())
str_3 = str(input())
str_4 = str(input())
str_5 = str(input())

if str_1 in str_2:
    if str_2 in str_3:
        if str_3 in str_4:
            if str_4 in str_5:
                print("magical")
            else:
                print("non-magical")
        else:
            print("non-magical")
    else:
        print("non-magical")
else:
    print("non-magical")
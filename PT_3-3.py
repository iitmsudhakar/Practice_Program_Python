'''Accept a string as input, print Integer if the string is an integer, print Float if it a float, else print None.
'''

n = input()

if '.' in n:
    print("Float")

elif n.isdigit:
    print("Integer")

elif n.isalpha:
    print("None")

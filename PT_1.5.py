'''
You are given a string and two non-negative integers as input.
The two integers specify the start and end indices of a substring in the given string.
Create a new string by replicating the substring a minimum number of times so that the resulting string is longer
than the input string.
The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive)
each on a different line.
'''

n = input()
str_l = len(n)
#print(str_l)
n1 = int(input())
n2 = int(input())

z = int(len(n))
new = n[n1:n2+1]
#print(new)

sub_str = ''

while len(sub_str) <= str_l:
    sub_str = sub_str + new

print(sub_str)



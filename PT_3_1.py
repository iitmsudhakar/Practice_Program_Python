# Palindrom check program

#functiont to conver string to list




def _str_list(s):
    L=[]
    for i in range(len(s)):
        L.append(s[i])
    return L

# function to check for odd even

def _odd_even(l):
    if len(l)%2 == 0:
        
        return True
    else:
        return False

# function to locate mid element

def _mid_elem(l):
    num = int(len(l))/2
    return num
   
   
def _mid(l):  
    if _odd_even(l):
        val = int(len(l))/2
        return int(val)
    else:
        val = int(len(l))/2
        val = val+0.5 -1
        return int(val)

#print(_mid(['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l','d']))

# function to check for Palindrom

def _palindrom(l):
    if _odd_even(l):
        if  l[_mid(l)] != l[_mid(l)+1] :
            print("NOT PALINDROME")
    elif not _odd_even(l):
        while len(l)>1:
            if l[0] ==l[-1]:
                l.pop(0)
                l.pop(-1)
        print("PALINDROME")


# palindrom check

def _palindrom2(l):
    flag = False
    while len(l)>=1:
        if l[0] ==l[-1]:
            l.pop(0)
            l.pop(-1)
            flag = True
        else:
            flag = False
    return flag    

word = _str_list(input())
if _palindrom2(word):
    print("PALINDROME")
else:
    print("NOT PALINDROME")


#_palindrom(['k','a','y','a','k','y'])



def some_function(word):
    space = ' ' # there is a single space between the quotes
    if space in word:
        return False
    # both letters 'A' and 'Z' are in upper case
    if not('A' <= word[0] <= 'Z'):
        return False
    for i in range(1, len(word)):
        # both letters 'a' and 'z' are in lower case
        if not('a' <= word[i] <= 'z'):
            return False
    return True


#print(some_function(input()))

def minmax(a, b):
    if a <= b:
        return a, b
    return b, a

#print(minmax(3,3))



def unique(L):
    L_uniq = [ ]
    for i in range(0, len(L)):
        if not(L[i] in L[i + 1: ]):
            L_uniq.append(L[i])
    return L_uniq

print(unique([1, 1, 2, 3, 5, 5]))
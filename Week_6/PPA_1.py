
freq = {}
words = input()
L = list(words.split(','))
S = set(L)

for elem in S:
    freq[elem] = 0
for x in L:
    freq[x]=freq[x]+1



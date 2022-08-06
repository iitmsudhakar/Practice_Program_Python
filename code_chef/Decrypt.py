n = int(input())
words = []
for i in range(n):
    w = input()
    words.append(w)
print(words)

#comparision
com_d1 = {}
com_d2 = {}
for i in words:
    com_d1[i] = 0

for i in words:
    for char in i:
        com_d2[char] = 0
for i in com_d1:
    for char in i:
        com_d2[char] += 1


print(com_d1)
print(com_d2)



encrypted = input().split(' ')
print(encrypted)

map_d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
enc_d = {}
for word in words:
    for char in word:
        if char in map_d:
            map_d[char] += 1

print(map_d)
# empty dictionary
for word in encrypted:
    for char in word:
        enc_d[char] = 0

for word in encrypted:
    for char in word:
        enc_d[char] += 1
print(enc_d)



'''
5
chef
had
bag
a
big
hdca deg e fib feb
D1 = {}

for i in range(len(words)):
    for char in words[i]:
        D1[char] = 0

for i in range(len(words)):
    for char in words[i]:
        D1[char] += 1

print(D1)



encrypted = input().split(' ')

D2 = {}

for i in range(len(encrypted)):
    for char in encrypted[i]:
        D2[char] = 0

for i in range(len(encrypted)):
    for char in encrypted[i]:
        D2[char] += 1

print(D2)

print(encrypted)

L1 ={}
for i in words:
    L1[i] = 0

for i in range(len(words)):
    L1[i] = len(L1[i])

print(L1)

for i in range(len(D1)):
    for j in range(len(D1)):
        pass
'''

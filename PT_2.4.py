def vowel_check(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    L = []
    for i in word:
        L.append(i)
    for v in vowels:
        if v in L:
            return True


def vowel_order(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    L = []
    NL = []
    for i in word:
        L.append(i)
    for w in L:
        if w in vowels:
            NL.append(w)
            # print(NL)
    if vowels == NL:
        return True


def count_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    L = []
    NL = []
    for i in word:
        L.append(i)
    for w in L:
        if w in vowels:
            NL.append(w)
    value = []
    for i in range(5):
        count = NL.count(vowels[i])
        value.append(count)
        # rint(value)
    count = 1
    if value[0] >= value[1]:
        count += 1
    if value[1] >= value[2]:
        count += 1
    if value[2] >= value[3]:
        count += 1
    if value[3] >= value[4]:
        count += 1
    if count == 5:
        return True


word = input()

print(vowel_check(word))
print(vowel_order(word))
print(count_vowel(word))

'''
if vowel_order(word) and vowel_check(word) and count_vowel(word):
    print("It is a perfect word")
else:
    print("It is not a perfect word")
'''
# vowel_order(word)

# print(vowel_check(word))


s = input()
a = 'aeiou'

f1 = True
for i in range(5):
    if a[i] not in s:
        f1 = False
        break

if f1:
    if s.index('a') < s.index('e') < s.index('i') < s.index('o') < s.index('u'):
        if s.count('a') >= s.count('e') >= s.count('i') >= s.count('o') >= s.count('u'):
            print('It is a perfect word')
        else:
            print('It is not a perfect word')

else:
    print('It is not a perfect word')

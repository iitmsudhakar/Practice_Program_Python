dic_1 = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
         'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p',
         'l': 'o', 'm': 'n'}

dic_2 = {'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd', 'v': 'e', 'u': 'f',
         't': 'g', 's': 'h', 'r': 'i', 'q': 'j', 'p': 'k',
         'o': 'l', 'n': 'm'}


word = input()

en_word = ''

for x in word:
    if x in dic_1:
        en_word += dic_1[x]
    else:
        en_word += dic_2[x]
print(en_word)
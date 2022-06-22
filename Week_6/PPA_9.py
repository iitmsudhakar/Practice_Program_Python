words = input().split(',')

real_dict = dict()

for word in words:
    first = words[0]
    if first not in real_dict:
        real_dict[first] = []
        real_dict[first].append(word)
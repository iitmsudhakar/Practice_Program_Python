



def distance(word_1, word_2):
    x = len(word_1)
    y = len(word_2)
    if x != y:
        return -1
    letters = "abcdefghijklmnopqrstuvwxyz"
    dist = 0
    for i in range (x):
        l1,l2 = word_1[i],word_2[i]
        d = abs(letters.index(l1) - letters.index(l2))
        dist += d
    return dist
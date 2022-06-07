num = input()
first, middle, last = int(num[0]), int(num[1]), int(num[2])
if first + last == middle:
    print('sandwich')
else:
    print('plain')
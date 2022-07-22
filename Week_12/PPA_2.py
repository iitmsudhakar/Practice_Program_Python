def rectangle(a, b):
    for i in range(1, a + 1):
        if i == 1 or i == a:
            print('o' * b)
        else:
            print('o', end='')
            print(' ' * (b - 2) + 'o')


a = int(input())
b = int(input())
rectangle(a, b)

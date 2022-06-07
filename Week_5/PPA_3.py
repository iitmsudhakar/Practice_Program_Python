def maxval(a, b, c):
    a = int(a)
    #print(a)
    b = int(b)
    #print(b)
    c = int(c)
    #print(c)
    list = [a,b,c]
    #print(list)
    max = a
    print(max)
    for num in list:
        if max < num:
            max = num
    print(max)

maxval(1, 2, 3)
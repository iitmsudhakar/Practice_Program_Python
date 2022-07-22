n = input().split(',')
m = []
while 'END' not in n:
    if len(n) == 2 and n[0] == 'JOIN':
        m.append(n[1])
    elif n[0] == "LEAVE":
        m.pop(0)
    elif len(n) == 3:
        member = n[1]
        m.remove(member)
        if n[2] == 'HEAD':
            m.insert(0, member)
        else:
            m.insert(len(m), member)

    if 'PRINT' in n:
        print(','.join(m))

    n = input().split(',')

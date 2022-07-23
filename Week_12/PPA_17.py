def final(n, moves):
    start = [1, 1]
    for d in moves:
        if d == 'N':
            if start[1] < n:
                start[1] += 1
        if d == 'S':
            if start[1] > 1:
                start[1] -= 1
        if d == 'E':
            if start[0] < n:
                start[0] += 1
        if d == 'W':
            if start[0] > 1:
                start[0] -= 1
        return start[0], start[1]

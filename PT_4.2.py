N = int(input())
L = input().split(',')


def check(N,L):
    count = 0
    for i in range(len(L)):
        for j in range(len(L)):
            if int(L[i])+int(L[j]) >= N:
                count += 1
    return count

print(check(N,L))
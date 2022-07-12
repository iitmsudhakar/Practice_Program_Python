a = int(input())
b = input().split(',')
total = 0
count = 0
for i in range(len(b)):
    for i in range(len(b) - 1):
        if int(b[i]) < int(b[i + 1]):
            b[i], b[i + 1] = b[i + 1], b[i]

for i in range(len(b)):
    total = total + int(b[i])
    count += 1
    if total >= a:
        print(count)
        break
else:
    print('None')

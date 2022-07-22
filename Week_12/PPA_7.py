num = input().split(',')

val = int(input())
l = []
for n in num:
    l.append(int(n))



if val > len(l):
    val = int(val % len(l))
    print(val)
l = (l[-val:] + l[:-val])

rot_l = ''

for x in range(len(l)-1):
    rot_l = rot_l + str(l[x]) + ','
rot_l += str(l[-1])

print(rot_l)

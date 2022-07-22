n = input()

L=n.split(',')

#print(L)

mid = int(int(len(L))/2)
end = int(len(L))
sum1 = 0
sum2 = 0
for i in range(0, mid):
    sum1 += int(L[i])

for j in range(mid,end):
    sum2 += int(L[j])

#print(sum1, sum2)

if sum1 == sum2:
    print("balanced")
if sum1 > sum2:
    print("left-heavy")
if sum1 < sum2:
    print("right-heavy")

#print(sum1,sum2)
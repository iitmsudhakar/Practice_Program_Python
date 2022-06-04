n = int(input())

L =[]
for num in range(n):
   # all prime numbers are greater than 1
   if num > 1:
       
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           L.append(num)
           #print(num)
           #print(L)
sum = 0
for i in range(len(L)):
    sum += L[i]

print(sum)
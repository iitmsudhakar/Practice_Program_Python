n = int(input())

f = open('C:\Users\ssudh\Documents\My Projects - Git\Practice Python Program\Practice_Program_Python\Week_9\files\pattern.txt', 'r')
count = 0
line = f.readlines()
while count !='':
    count += 1
    line = line.strip()
    if count == n:
        print(line)
f.close()
print("None")
    

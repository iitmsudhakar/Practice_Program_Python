number = input()

count = 0

for x in number:
    if x == 'l' or x == 'o':
        count += 1



if count == 0:
    print("No Mistakes")
else:
    print(f"{count} mistakes")
    for x in number:
        if x == 'l':
            number = number.replace('l','1')
        if x == 'o':
            number = number.replace('o','0')
    print(number)







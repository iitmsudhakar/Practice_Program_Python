word = 'one,two,order,reat,tong,tight,tree,cool,lot,trouble'
word = word.split(',')
#print(word)

nl = []
l=[]
for i in range(len(word)):
    x = ''
    if i != len(word) - 1:
        #print(word[i][-1])
        #print(word[i+1][0])
        if word[i][-1] == word[i+1][0]:
            x = word[i]
            l.append(x)
            nl.append(l)
        else:
            l = []
min = 0
for i in range(len(nl)):
    if len(nl[i]) > min:
        min = len(nl[i])

min = min+1
print((min))
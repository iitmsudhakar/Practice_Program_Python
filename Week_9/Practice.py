import string

def create_num_dictionary(k):
    k = int(k)
    # Create alphabets of English in lower case
    lst = []
    for i in range(11):
        lst.append(i)
    num_d = {}
    for i in range (len(lst)):
        num_d[lst[i]] = lst[(i+k)%10]
    return num_d


def create_dictionary(k):
    # Key converted to integer
    k = int(k)
    # Create alphabets of English in lower case
    l = string.ascii_lowercase
    # Covert strings to list
    l = list(l)
    # Declare a empty dictionary
    d = {}
    # Iterate through list and create the dictionary with value
    for i in range (len(l)):
        d[l[i]] = l[(i+k)%26]
    return d
'''
spl = '[@_!#$%^&*()''<>?/\|}{~:""]'
spl_d = {}
for i in spl:
    spl_d[i] = i
f = open('testfile.txt','r')
g = open("Encrypted_File.txt",'w')
d = create_dictionary('3')
c = f.read(1)
while (c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()

'''

print(create_num_dictionary('4'))
import string

def decrypt_char(k):
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
        d[l[i]] = l[(i-k)%26]
    return d
# Funtion to generate the dictionary of number with Casear Chipher logic
def decrypt_num(k):
    k = int(k)
    num = '0123456789'
    lst = []
    for i in num:
        lst.append(i)
    num_d = {}
    for i in range (len(lst)):
        num_d[lst[i]] = lst[(i-k)%10]
    return num_d

# Get the input from user
source_file = input("Enter the text file name with externtion: ")
print(source_file)
k = int(input('Enter the secret key value: '))
print(k)
# File Handling
f = open(source_file,'r')
# Create the Encrypted file
g = open("Decrypted_File.txt",'w')

# Call the dictionary creation functions
d = decrypt_char(k)
num_d = decrypt_num(k)

# Handling of special characters
spl = ' [@_!#$%^,â=&*()+-.€\'\'<>?/\|}{~:;""]'
spl_d = {}
for i in spl:
    spl_d[i] = i

# Encryption logic
c=f.read(1)
while c !='':   
    # Handling special characters    
    if c in spl:
        g.write(spl_d[c])
        c=f.read(1)
    # Handling numbers
    elif c in num_d:
        g.write(num_d[c])
        c=f.read(1)
    # Handling alpha characters
    elif c.isalpha:
        c = c.lower()
        g.write(d[c])
        c=f.read(1)
# Close the files
f.close()
g.close()



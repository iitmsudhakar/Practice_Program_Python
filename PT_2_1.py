# create a list of n integers for each grouping logic
def _sapphire_(n):
    sapphire_List = list(range(1,n+1,4))
    return sapphire_List

def _peridot_(n):
    peridot_List = list(range(2,n+1,4))
    return peridot_List

def _ruby_(n):
    ruby_List = list(range(3,n+1,4))
    return ruby_List

def _emerald_(n):
    emerald_List = list(range(4,n+1,4))
    return emerald_List

# input roll number from user

number = int(input())

# print roll number based on grouping 
if number in _sapphire_(number):
    print("Sapphire")

if number in _peridot_(number):
    print("Peridot")

if number in _ruby_(number):
    print("Ruby")

if number in _emerald_(number):
    print("Emerald")
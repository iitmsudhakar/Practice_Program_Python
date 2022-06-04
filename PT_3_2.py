def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    if gcd(x, y) == 1:
        print("Coprime")
    else:
        print("Not Coprime")
    

n1 = int(input())
n2 = int(input())

is_coprime(n1, n2)
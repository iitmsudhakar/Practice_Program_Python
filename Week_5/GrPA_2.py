
def _factors(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum


def is_perfect(n):
    x =_factors(n)
    if x == n:
        return True
    else:
        return False



print(is_perfect(int(input())))
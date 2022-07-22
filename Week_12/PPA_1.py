def _isprime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


def primes_galore(L):
    count = 0
    for i in range(2, len(L)):
        if _isprime(i) and _isprime(L[i]):
            count += 1
    return count


print(count)

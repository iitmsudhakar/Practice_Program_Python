def collatz(n):
    if n == 2:
        return 1
    else:
        if n % 2 != 0:
            C = 1 + collatz((3*n)+1)
            return C
        else:

            C = 1 + collatz(n/2) 
            return C
    
    



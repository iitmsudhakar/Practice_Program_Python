def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(n):
        psum = psum + L[i] * (x_0 ** i)
    return psum


    
def poly_zeros(L, a, b):
    zeros = [ ]
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros


print(poly_zeros([2, -3, 1], 0, 4))

#print(poly([1, 2, 3], 5))
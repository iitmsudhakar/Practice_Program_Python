def _dsum(mat):
    dim = len(mat)
    d_sum_1, d_sum_2 = 0, 0
    for i in range(dim):
        d_sum_1 += mat[i][i]
        d_sum_2 += mat[i][dim-i-1]
    if d_sum_1 == d_sum_2:
        return True
    else:
        return False

def _r_c_sum(mat):
    dim = len(mat)
    r_sum, c_sum = 0, 0
    for i in range(dim):
        for j in range(dim):
            r_sum += mat[i][j]
            c_sum += mat[j][i]
    if r_sum == c_sum:
        return True
    else:
        return False

def is_magic(mat):
    if _dsum(mat) and _r_c_sum(mat):
        return 'YES'
    else:
        return 'NO'




mat = [[1,4,2],[4,5,3],[6,2,9]]

print(_dsum(mat))
print(_r_c_sum(mat))


def is_magic(mat): 
    m = len(mat) 
    # the sum of the two diagonals
    d1sum, d2sum = 0, 0 
    # (i, i) goes from top-left 
    # (i, m - i - 1) goes from top
    # note that a single loop is enough; no ne
    for i in range(m): 
        d1sum += mat[i][i] 
        d2sum += mat[i][m - i -1]
    # if the two diagonal sums are unequal, we can return NO
    # unnecessary computation can be avoided
        if not(d1sum == d2sum):
            return 'NO' 
    # get row-sum and column
    for i in range(m): 
        rsum, csum = 0, 0 
        for j in range(m): 
            rsum += mat[i][j] 
            csum += mat[j][i] 
        if not(rsum == csum == d1sum):
            return 'NO' 
        else:
            return 'YES'
def maxDivisor(l, r, d):
    i=r
    while i>=l:
        if i%d==0:
            return i
        i-=1
    return -1

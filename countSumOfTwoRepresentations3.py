def countSumOfTwoRepresentations3(n, l, r):
    j=min(r,n-l)-max(l,n-r)
    if j>=0:
        return j/2+1
    return 0

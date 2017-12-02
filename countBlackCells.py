def countBlackCells(n, m):
    s=n+m
    while m:
        n%=m
        n,m=m,n
    return s-n+2*(n-1)

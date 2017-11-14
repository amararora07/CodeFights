def halvingSum(n):
    s=0
    while n > 0:
        s+=n
        n/=2
    return s

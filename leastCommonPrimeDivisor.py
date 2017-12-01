def leastCommonPrimeDivisor(a, b):
    d=2
    while a>1 and b>1:
        if a%d== 0 and b%d==0:
            return d
        while a%d==0:
            a/=d
        while b%d==0:
            b/=d
        d+= 1
    return -1

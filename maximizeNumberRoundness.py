def maximizeNumberRoundness(n):
    t,z=n,0
    while t>0:
        if t%10==0:
            z+=1
        t/=10
    r=z
    for i in range(z):
        if n%10==0:
            r-=1
        n/=10
    return r

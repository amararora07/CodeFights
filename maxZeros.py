def maxZeros(n):
    a,m=0,0
    for i in range(2,n+1):
        t,v=0,n
        while v>0:
            if v%i==0:
                t+=1
            v/=i
        if t>m:
            m=t
            a=i
    return a

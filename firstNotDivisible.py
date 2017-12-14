def firstNotDivisible(d, start):
    t=1
    while 1:
        c=1
        for i in range(len(d)):
            if t%d[i]==0:
                c=0
                break
        if c:
            return t
        t+=1

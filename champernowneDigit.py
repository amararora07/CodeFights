def champernowneDigit(n):
    i = 1
    while 1:
        t=i
        l=[]
        while t>0:
            l.append(t%10)
            t/=10
        l.reverse()
        if n<=len(l):
            return l[n - 1]
        n -= len(digits)
        i += 1

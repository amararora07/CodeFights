def uniqueDigitProducts(a):
    l=[]
    for i in a:
        z,p=i,1
        while z>0:
            p*=(z%10)
            z/=10
        if p not in l:
            l.append(p)
    return len(l)

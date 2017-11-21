def isDivisibleBy3(s):
    d=0
    l=list(s)
    for i in range(len(l)):
        if l[i]!="*":
            d+=int(l[i])
    x=[]
    e=l.index("*")
    for i in range(10):
        f=l
        if (i+d)%3==0:
            f[e]=str(i)
            x.append("".join(l))
    return x

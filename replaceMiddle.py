def replaceMiddle(a):
    if len(a)%2!=0:
        return a
    s=[]
    sm=(len(a)-1)/2
    sm1=len(a)/2
    tot=a[sm]+a[sm1]
    for i in range(len(a)):
        if i==sm1:
            continue
        elif i==sm:
            s.append(tot)
        else:
            s.append(a[i])
    return s

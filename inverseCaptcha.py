def inverseCaptcha(a):
    l=[]
    while a>0:
        l.append(a%10)
        a/=10
    s=[]
    l.append(l[0])
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            s.append(l[i])
    return sum(s)

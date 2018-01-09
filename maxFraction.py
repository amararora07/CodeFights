def maxFraction(a, b):
    s=[]
    for i in range(len(a)):
        s.append(a[i]*1.0/b[i])
    return s.index(max(s))

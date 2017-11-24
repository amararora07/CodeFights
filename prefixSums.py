def prefixSums(a):
    s=[]
    for i in range(0,len(a)):
        s.append(sum(a[0:i+1]))
    return s

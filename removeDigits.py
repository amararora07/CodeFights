def removeDigits(n, k):
    l=[]
    n=str(n)
    for i in range(len(n)-k+1):
        l.append(int(n[i:i+k]))
    return [min(l),max(l)]

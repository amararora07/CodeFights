def eratosthenesSieve(n):
    p=[True]*(n+1)
    i=2
    while i*i<=n:
        if p[i]==True:
            j=i*2
            while j<=n:
                p[j]=False
                j+=i
        i+=1
    s=[]
    for i in range(2,n+1):
        if p[i]:
            s.append(i)
    return s

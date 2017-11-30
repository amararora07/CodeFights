def checkFactorial(n):
    l,s=1,1
    while l<n:
        l*=s
        s+=1
    return l==n

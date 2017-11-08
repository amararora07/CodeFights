def powersOfTwo(n):
    l=1
    while l<n: 
        l*=2
    s=[]
    while n:
        while l>n:
            l/=2
        s.append(l)
        n-=l
    return s[::-1]

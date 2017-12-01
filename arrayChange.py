def arrayChange(a):
    c=0
    for i in range(len(a)-1):
        l=a[i]
        r=a[i+1]    
        if l>=r:
            t=l-r+1
            a[i+1]+=t
            c+=t
    return c

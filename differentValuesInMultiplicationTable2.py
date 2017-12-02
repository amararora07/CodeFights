def differentValuesInMultiplicationTable2(n, m):
    a=[0]*(n*m+1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i*j]=1
    s=0
    for i in range(1,n*m+1):
        if a[i]:
            s+=1
    return s

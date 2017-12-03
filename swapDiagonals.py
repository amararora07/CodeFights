def swapDiagonals(m):
    for i in range(len(m)):
        t=m[i][len(m[0])-i-1]
        m[i][len(m[0])-i-1]=m[i][i]
        m[i][i]=t
    return m

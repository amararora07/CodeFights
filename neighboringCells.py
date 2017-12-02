def neighboringCells(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            c=0
            if i-1>=0:
                c+=1
            if i+1<len(m):
                c+=1
            if j-1>=0:
                c+=1
            if j+1<len(m[0]):
                c+=1
            m[i][j]=c
    return m

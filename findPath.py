def findPath(m):
    n=len(m)
    l=len(m[0])
    p=[[0,0] for i in range(n*l)]
    for i in range(n):
        for j in range(l):
            p[m[i][j]-1][0] = i
            p[m[i][j]-1][1] = j
            
    for i in range(n*l-1):
        if abs(p[i][0]-p[i+1][0]) + abs(p[i][1]-p[i+1][1]) > 1:
            return False
    return True

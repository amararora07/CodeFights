def isSkewSymmetricMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!=-1*m[j][i]:
                return False
    return True

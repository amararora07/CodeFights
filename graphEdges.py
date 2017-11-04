def graphEdges(matrix):
    s=0
    for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                if matrix[i][j]:
                    s+=1
    return s

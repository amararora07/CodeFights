def crossingSum(matrix, a, b):
    s,d=sum(matrix[a]),0
    for i in range(len(matrix)):
        if i!=a:
            d+=matrix[i][b]
    return s+d

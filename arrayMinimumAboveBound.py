def arrayMinimumAboveBound(inputArray, bound):
    m=100000
    for i in inputArray:
        if i > bound and i < m:
            m=i
    return m

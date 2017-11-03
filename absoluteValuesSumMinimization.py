def absoluteValuesSumMinimization(a):
    a.sort()
    d=len(a)
    if d%2==1:
        return a[d/2]
    else:
        return a[d/2 - 1]

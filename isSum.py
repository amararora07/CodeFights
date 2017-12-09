def isSum(value):
    s,a=0,False
    for i in range(value+1):
        s+=i
        if s==value:
            a=True
    return a

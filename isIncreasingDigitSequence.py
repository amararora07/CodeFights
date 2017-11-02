def isIncreasingDigitsSequence(n):
    if n==0:
        return True
    l=[]
    while n > 0:
        l.append(n%10)
        n/=10
    m=l[::-1]
    for i in range(len(m)-1):
        if m[i] >= m[i+1]:
            return False
    else:
        return True

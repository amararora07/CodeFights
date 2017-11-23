def isIncreasingDigitsSequence(n):
    l=list(str(n))
    for i in range(len(l)-1):
        if ord(l[i])>=ord(l[i+1]):
            return False
    return True

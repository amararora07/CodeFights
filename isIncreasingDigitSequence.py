def isIncreasingDigitsSequence(n):
    n=str(n)
    return all(n[i-1]<n[i] for i in range(1,len(n)))

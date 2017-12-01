def arrayMaxConsecutiveSum(a, k):
    m=s=sum(a[0:k])
    for i in range(k, len(a)):
        s-=a[i-k]
        s+=a[i]
        if s>m:
            m=s
    return m

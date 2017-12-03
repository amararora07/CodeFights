def kthDigit(n, k):
    l=str(n)
    if len(l)<k:
        return -1
    return int(l[k-1])

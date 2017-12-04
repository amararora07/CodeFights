def lrSegmentNumber(l, r):
    s=''
    while l<=r:
        s+=str(l)
        l+=1
    return int(s)

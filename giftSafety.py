def giftSafety(t):
    l=0
    while len(t)>2:
        l+=len(set(t[:3]))<3
        t = t[1:]
    return l

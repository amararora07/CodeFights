def squareDigitsSequence(a0):
    a=a0
    d=set()
    while not (a in d):
        d.add(a)
        nxt=0
        while a>0:
            nxt+=(a%10)*(a%10)
            a/=10
        a=nxt
    return len(d)+1

def toAndFro(a, b, t):
    l=(t/(b-a))%2!=0
    d=t%(b-a)
    if l:
        return b-d 
    else:
        return a+d

def appleBoxes(k):
    s,d=0,0
    while d<=k:
        if d%2==0:
            s+=d*d
        else:
            s-=d*d
        d+=1
    return s

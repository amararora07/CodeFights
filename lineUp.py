def lineUp(commands):
    l=0
    r=0
    d={'L':3,'A':2,'R':1}
    for i in commands:
        r+=d[i]
        if r%2==0:
            l+=1
    return l

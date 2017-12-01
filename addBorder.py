def addBorder(pic):
    l=[]
    s=""
    for i in range(len(pic[0])+2):
        s+="*"
    l.append(s)
    for i in range(len(pic)):
        r="*"
        for j in range(len(pic[0])):
            r+=pic[i][j]
        r+="*"
        l.append(r)
    l.append(s)
    return l

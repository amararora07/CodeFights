def delivery(o, s):
    if len(o)==0 or len(s)==0:
        return False
    l=[]
    x=o[1]+o[2]
    for i in range(len(s)):
        d=(float(o[0]+s[i][0])/float(s[i][1]))+s[i][2]
        if d<o[1]:
            l.append(False)
        elif d>=o[1] and d<=x:
            l.append(True)
        else:
            l.append(False)
    return l

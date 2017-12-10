def arrayCenter(a):
    l=[]
    avg=(sum(a)*1.0)/len(a)
    for i in a:
        if abs(i-avg)<min(a):
            l.append(i)
    return l

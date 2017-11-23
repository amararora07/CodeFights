def smallestUnusualNumber(a):
    l=map(int,list(a))
    #print l
    s=sum(l)
    b=l[0]
    for i in range(1,len(l)):
        b*=l[i]
    if s>b:
        return 0
    return 10-l[-1]

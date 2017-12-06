def numbersGrouping(a):
    l=[0]*100000
    for i in range(len(a)):
        d=(a[i]-1)/10000
        if l[d]==0:
            l[d]+=2
        else:
            l[d]+=1
    return sum(l)

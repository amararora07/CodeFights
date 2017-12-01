def extractEachKth(a,k):
    l=[]
    for i in range(len(a)):
        if (i+1)%k:
            l+=[a[i]]
    return l

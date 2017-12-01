def arrayReplace(a,e,s):
    l=a
    for i in range(len(a)):
        if a[i]==e:
            l[i]=s
    return l

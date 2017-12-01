def areSimilar(a, b):
    d=[0]*1000
    e=[0]*1000
    c=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            d[c]=a[i]
            e[c]=b[i]
            c+=1
            if c>2:
                return False
    return d[0]==e[1] and d[1]==e[0]

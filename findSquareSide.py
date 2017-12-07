def findSquareSide(x, y):
    def sq(a,b,c,d):
        return (c-a)**2+(d-b)**2
    l=10000000
    for i in range(len(x)):
        l=min(l,sq(x[i],y[i],x[i-1],y[i-1]))
    return l

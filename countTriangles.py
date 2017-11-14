def countTriangles(x, y):
    s=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                a=x[i]-x[j]
                b=x[i]-x[k]
                c=y[i]-y[j]
                d=y[i]-y[k]
                if a*d!=b*c:
                    s+=1
    return s

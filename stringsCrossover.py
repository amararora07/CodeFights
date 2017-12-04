def stringsCrossover(a, r):
    l=0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            d=True
            for k in range(len(r)):
                if a[i][k]==r[k] or a[j][k]==r[k]:
                    continue
                else:
                    d=False
            if d:
                l+=1
    return l

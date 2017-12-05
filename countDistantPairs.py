def countDistantPairs(a, d):
    s=0
    for i in range(len(a)-d-1):
        if a[i]==a[i+d+1]:
            s+=1
    return s

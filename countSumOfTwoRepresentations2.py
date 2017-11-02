def countSumOfTwoRepresentations2(n, l, r):
    s=0
    for i in range(l,r+1):
        x=n-i
        if x>=l and x<=r and x>=i:
            s+=1
    return s

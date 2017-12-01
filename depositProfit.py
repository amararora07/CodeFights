def depositProfit(d,r,t):
    s=0
    while d<t:
        d+=(d*r)/100.0
        s+=1
    return s

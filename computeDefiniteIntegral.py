def computeDefiniteIntegral(l, r, p):
    s=0
    for i in range(len(p)):
        s+=p[i]*((r*1.0)**(i+1)-l**(i+1))/(i+1)
    return s

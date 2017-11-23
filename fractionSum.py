def fractionSum(a, b):
    c=[(a[0]*b[1])+(a[1]*b[0]),a[1]*b[1]]
    gcd2=gcd(c[0],c[1])
    c[0]/=gcd2
    c[1]/=gcd2
    return c
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

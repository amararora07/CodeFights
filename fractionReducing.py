def fractionReducing(f):
    gcd2=gcd(f[0],f[1])
    f[0]/=gcd2
    f[1]/=gcd2
    return f
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

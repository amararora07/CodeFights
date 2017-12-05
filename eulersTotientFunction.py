from fractions import gcd
def eulersTotientFunction(n):
    l=[i for i in range(1,n+1) if i<=n and gcd(n,i)==1]
    return len(l)

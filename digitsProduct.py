def digitsProduct(a):
    max=5000
    for i in range(1,max):
        if a==pro(i):
            return i
    return -1
def pro(n):
    p=1
    while n>0:
        p=p*(n%10)
        n/=10
    return p

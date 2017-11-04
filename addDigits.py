def addDigits(a, b, n):
    while n>0:
        for i in range(9,-1,-1):
            t = a*10 + i
            if t % b == 0:
                a=t
                break
        n-=1
    return str(a)

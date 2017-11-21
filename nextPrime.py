def nextPrime(n):
    i=n+1
    while True:
        p=1
        j=2
        while j*j<=i:
            if i%j==0:
                p=False
                break
            j+=1
        if p:
            return i
        i+=1

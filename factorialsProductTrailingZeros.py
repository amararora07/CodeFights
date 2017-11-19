def factorialsProductTrailingZeros(l, r):
    x=1
    for i in range(l,r+1):
        x*=math.factorial(i)
    r=0
    d=list(str(x))
    for i in d[::-1]:
        if i!='0':
            return r
        else:
            r+=1

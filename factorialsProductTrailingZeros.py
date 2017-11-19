def factorialsProductTrailingZeros(l, r):
    x=1
    for i in range(l,r+1):
        x*=math.factorial(i)
    r=0
    d=list(str(x))
    d=d[::-1]
    for i in d:
        if i=='0':
            r+=1
        else:
            break
    return  r

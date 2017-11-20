def maxSubarray(inp):
    s=0
    d=0
    for i in inp:
        s+=i
        if s<0:
            s=0
        if s>d:
            d=s
    return d

def exerciseElaboration(p, n):
    s=str('0')*n
    res=str(p)+s+str(p)
    return sum([int(i) for i in str(int(res)**2)])

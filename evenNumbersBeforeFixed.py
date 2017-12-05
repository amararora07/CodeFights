def evenNumbersBeforeFixed(s, f):
    if f not in s:
        return -1
    j=s.index(f)
    c=0
    for i in range(j):
        if s[i]%2 == 0:print s[i]
            c+=1
    return c

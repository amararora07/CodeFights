def isOneSwapEnough(inp):
    l=list(inp)
    if ispalin(l):
        return True
    for i in range(len(l)):
        for j in range(len(l)):
            s=l[:]
            s[i]=l[j]
            s[j]=l[i]
            if ispalin(s):
                return True
    return False
def ispalin(a):
    if a==a[::-1]:
        return True

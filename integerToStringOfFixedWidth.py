def integerToStringOfFixedWidth(n,v):
    n=str(n)
    if len(n)==v:
        return n
    s=""
    if v>len(n):
        s+='0'*(v-len(n))
        s+=n
        return s
    n=n[::-1]
    n=n[:v]
    n=n[::-1]
    return n

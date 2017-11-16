def alphabeticShift(inp):
    s=""
    z='abcdefghijklmnopqrstuvwxyz'
    x='bcdefghijklmnopqrstuvwxyza'
    for i in range(len(inp)):
        if inp[i] in z:
            t=z.index(inp[i])
            s+=x[t]
    return s

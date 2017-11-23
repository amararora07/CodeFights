def bishopAndPawn(b,p):
    e=ord(b[0])-65
    f=ord(b[1])-49
    g=ord(p[0])-65
    h=ord(p[1])-49
    if (e+f)==(g+h) or (e-f)==(g-h):
        return True
    return False

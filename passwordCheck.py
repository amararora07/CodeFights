def passwordCheck(inp):
    a,b,c,d=0,0,0,len(inp)
    e=True
    if d<5:
        e=False
    for i in range(len(inp)):
        if inp[i].isupper():
            a=1
        elif inp[i].islower():
            b=1
        elif ord(inp[i]) >= 48 and ord(inp[i])<=57:
            c=1
    return a and b and c and e

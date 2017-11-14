def isIPv4Address(inp):
    l=inp.split(".")
    print l
    if len(l)==4:
        x=0
        for i in l:
            if i.isdigit() and 0<=int(i)<=255:
                x+=1
        if x==len(l):
            return True
    return False

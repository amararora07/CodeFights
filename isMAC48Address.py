def isMAC48Address(inp):
    x="0123456789ABCDEF"
    l=inp.split("-")
    if len(l)!=6:
        return False
    for i in l:
        if len(i)!=2:
            return False
        if i[0] not in x or i[1] not in x:
            return False
    return True

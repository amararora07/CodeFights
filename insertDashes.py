def insertDashes(inp):
    l=inp.split()
    for i in range(len(l)):
        l[i]='-'.join(list(l[i]))
    return " ".join(l)

def differentSubstrings(inp):
    l=[]
    s=0
    for i in range(len(inp)):
        for j in range(i-1,len(inp)+1):
            l.append(inp[i:j])
    l.sort()
    for i in range(1, len(l)):
        if l[i]!=l[i - 1]:
            s += 1
    return s

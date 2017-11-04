def allLongestStrings(inp):
    l,d=[],[]
    for i in inp:
        l.append(len(i))
    s=max(l)
    for i in inp:
        if len(i)==s:
            d.append(i)
    return d

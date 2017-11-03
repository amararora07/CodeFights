def differentSymbolsNaive(s):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    s=set()
    for i in l:
        if i not in s:
            s.add(i)
    return len(s)

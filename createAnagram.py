def createAnagram(s, t):
    l=[i for i in s]
    for i in t:
        if i in l:
            l.pop(l.index(i))
    return len(l)

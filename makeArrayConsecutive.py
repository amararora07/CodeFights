def makeArrayConsecutive(s):
    l=[]
    s.sort()
    for i in range(s[0],s[len(s)-1]):
        if i not in s:
            l.append(i)
    return l

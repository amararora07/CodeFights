def makeArrayConsecutive(s):
    s.sort()
    c=0
    l=[]
    for i in range(s[0],s[len(s)-1]):
      if s[c]!=i:
        l.append(i)
      else:
        c+=1
    return l

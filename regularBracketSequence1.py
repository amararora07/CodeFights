def regularBracketSequence1(s):
    l=0
    for i in range(len(s)):
        if s[i]=="(":
            l+=1
        else:
          l-=1
        if l<0:
          return False
    if l:
      return False
    return True

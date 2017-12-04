def reduceString(s):
    if len(s)<1:
        return s
    if s[0]==s[-1]:
        return reduceString(s[1:-1]) 
    return s

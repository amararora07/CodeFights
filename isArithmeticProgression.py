def isArithmeticProgression(s):
    d=s[1]-s[0]
    for i in range(2,len(s)):
        if s[i]-s[i-1]!=d:
            return False
    return True

def sameDigitNumber(n):
    s=[]
    while n>0:
        s.append(n%10)
        n/=10
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            return False
    return True

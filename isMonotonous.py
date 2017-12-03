def isMonotonous(s):
    a,b=0,0
    for i in range(1,len(s)):
        if s[i]>s[i-1]: a+=1
        if s[i]<s[i-1]: b+=1
    if a==len(s)-1 or b==len(s)-1:
        return True
    return False

def isBeautifulString(a):
    res=True
    for i in range(97,122):
        n=chr(i+1)
        if count(a,chr(i))<count(a,n):
            res=False
            break
    return res
def count(s,c):
    count=0
    for i in range(len(s)):
        if s[i]==c:
            count+=1
    return count

def differentDigitsNumberSearch(a):
    for i in a:
        n=i
        s=set()
        l=[]
        while n>0:
            s.add(n%10)
            l.append(n%10)
            n/=10
        if len(s)==len(l):
            return i
    return -1

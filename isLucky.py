def isLucky(n):
    l=[]
    while n>0:
        l.append(n%10)
        n/=10
    return sum(l[0:len(l)/2])==sum(l[len(l)/2:len(l)])

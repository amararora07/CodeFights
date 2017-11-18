def isSumOfConsecutive(n):
    for i in range(1,n):
        t,s=n,i
        while t>0:
            t-=s
            s+=1
        if t==0:
            return True
    return False

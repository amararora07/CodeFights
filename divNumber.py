def divNumber(k, l, r):
    count=0 
    for i in range(l,r+1):
        if total(i)==k:
            count+=1
    return count
def total(a):
    c=0
    for i in range(1,a/2):
        if a%i==0:
            c+=1
    return c

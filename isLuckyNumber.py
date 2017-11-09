def isLuckyNumber(n):
    while n>0:
        r=n%10
        if r!=4 and r!=7:
            return False
        n/=10
    return True

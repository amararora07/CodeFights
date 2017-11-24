def increaseNumberRoundness(n):
    a=0
    while n>0:
        if n%10==0 and a:
            return True
        elif n%10!=0:
            a=1
        n/=10
    return False

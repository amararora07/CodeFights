def isInfiniteProcess(a, b):
    if 0<=a<=20 and 0<=b<=20:
        if b>=a and (b-a)%2==0:
            return False
        else:
            return True

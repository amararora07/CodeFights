def sumBelowBound(b):
    s=0
    for i in range(100):
        s+=i
        if s>b:
            return i-1

def smallestMultiple(left, right):
    for i in range(1,1000000):
        s=True
        for j in range(left,right+1):
            if i%j!=0:
                s=False
        if s:
            return i

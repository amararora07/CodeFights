def directionOfReading(numbers):
    l=[]
    for i in range(len(numbers)):
        s=""
        for j in numbers:
            s+=str((j%10**(i+1))//10**i)
        l.append(int(s))
    l.reverse()
    return l

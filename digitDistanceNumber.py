def digitDistanceNumber(n):
    s=""
    d=str(n)
    for i in range(len(d)-1):
        s+=str(abs(int(d[i+1])- int(d[i])))
        
    return int(s)

def swapNeighbouringDigits(n):
    s=str(n)
    t=''
    for i in range(int(len(s)/2)):
        t+=s[i*2+1]+s[i*2]
    return int(t)

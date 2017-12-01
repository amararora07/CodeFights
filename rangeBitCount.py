def rangeBitCount(a, b):
    l=[]
    for i in range(a,b+1):
        l.append(bin(i)[2:])
    s=0
    for i in l:
        for j in range(len(i)):
            if i[j]=='1':
                s+=1
    return s

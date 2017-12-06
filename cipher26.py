def cipher26(m):
    s=""
    a,b=0,0
    for i in range(len(m)):
        t=ord(m[i])-97
        a=t-b
        if a<0:
            a+=26
        s+=chr(a+97)
        b=t
    return s

def strangeCode(s, e):
    l=""
    i="a"
    while s<e-1:
        s+=1
        e-=1
        l+=i
        if i=="a":
            i="b"
        else i="a"
    return l

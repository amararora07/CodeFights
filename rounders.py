def rounders(v):
    l=10
    while v>l:
        if ((v%l)/(l/10))<5:
            v=(v/l)*l
        else:
            v=(v/l+1)*l
        l*=10
    return v

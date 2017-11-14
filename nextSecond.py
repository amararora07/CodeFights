def nextSecond(c):
    if c[2]==59:
        c[2]=0
        if c[1]==59:
            c[1]=0
            if c[0]==23:
                c[0]=0
            else:
                c[0]+=1
        else:
            c[1]+=1
    else:
        c[2]+=1
    return c

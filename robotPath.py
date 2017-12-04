def robotPath(ins, b):
    dx,dy,x,y=[-1,0,1,0],[0,1,0,-1],0,0
    st='LURD'
    for i in range(len(ins)):
        a=0
        for j in range(1,4):
            if ins[i]==st[j]:
                a=j
        if abs(x+dx[a])<=b and abs(y+dy[a])<=b:
            x+=dx[a]
            y+=dy[a]
    return [x,y]

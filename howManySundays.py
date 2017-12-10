def howManySundays(n, s):
    l=['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
    j=-1
    for i in range(len(l)):
        if l[i]==s:
            j=i
            break
    return (j+n)/len(l)

def companyBotStrategy(train):
    l,t,n=0,0,0.0
    
    for i in range(len(train)):
        if train[i][1]==1:
            l+=1
            t+=train[i][0]
    if l>0:
        n=float(t)/float(l)
    return n

def electionsWinners(votes, k):
    t=0
    for i in range(len(votes)):
        t=max(t,votes[i])
    a=0
    for i in range(len(votes)):
        if votes[i]+k>t:
            a+=1
    if a==0:
        for i in range(len(votes)):
            if votes[i]==t:
                a+=1
        if a>1:
            a=0
    return a

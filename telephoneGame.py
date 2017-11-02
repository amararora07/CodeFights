def telephoneGame(messages):
    t=-1
    for i in range(len(messages)-1):
        if messages[i]!=messages[i+1]:
            t=i+1
            break
    return t

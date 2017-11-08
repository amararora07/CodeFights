def isTandemRepeat(inp):
    t=len(inp)
    if t % 2 == 1:
        return False
    for i in range(0,t/2):
        if inp[i]!=inp[i-(t/2)]:
            return False
    else:
        return True

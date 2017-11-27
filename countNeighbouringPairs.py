def countNeighbouringPairs(inp):
    l=0
    for i in range(len(inp)-1):
        if inp[i]==inp[i+1]:
            l+=1
    return l

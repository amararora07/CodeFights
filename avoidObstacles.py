def avoidObstacles(inp):
    j=max(inp)
    for i in range(1,j):
        a=any([d for d in inp if d%i==0])
        if not a:
            return i
    return max(inp)+1

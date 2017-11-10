def equationSolutions(l, r):
    res = 0
    for i in range(l,r+1):
        j = l
        while j <= r:
            if i**3 == j**2:
                res += 1
            j += 1
    return res

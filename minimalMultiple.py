def minimalMultiple(d, l):

    if l%d == 0:
        return l
    return (l/d+1)*d

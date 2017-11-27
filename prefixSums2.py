def prefixSums(a):

    b = [ a[0] ]
    for i in range(1, len(a)):
        b.append( a[i]+b[-1] )

    return b

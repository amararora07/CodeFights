def fixedPointsPermutation(permutation):
    res=0
    for i in range(len(permutation)):
        if i+1==permutation[i]:
            res+=1
    return res

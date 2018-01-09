def permutationShift(per):
    l=[]
    for i in range(len(per)):
        l+=[per[i]-i]
    return max(l)-min(l)

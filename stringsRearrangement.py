import itertools as it
def stringsRearrangement(a):
    for p in it.permutations(a):
        if all([sum([i!=j for i,j in zip(*q)])==1 for q in zip(p[:-1],p[1:]) ]):
            return True
    return False 

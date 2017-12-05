from itertools import permutations as p
def equationTemplate(v):
    for i in p(v,4):
        if i[0]*i[1]*i[2]==x[3]:
            return True
        elif i[0]*i[1]==i[2]*i[3]:
            return True
    return False

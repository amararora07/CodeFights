def quadraticEquation(a, b, c):
    d=b**2-4*a*c
    if d<0:
        return []
    else:
        x=(-b+math.sqrt(d))/(2*a)
        y=(-b-math.sqrt(d))/(2*a)
        if x==y:
            return [x]
        return sorted([x,y])

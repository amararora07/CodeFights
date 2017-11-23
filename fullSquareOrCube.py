import itertools
def fullSquareOrCube(n):
    s=str(number)
    a,b=set(),set()
    for i in itertools.permutations(s):
        a.add(int(''.join(list(i))))
    for i in range (1, 33):
        if i**2 in a:
            b.add (i**2)
        if i**3 in a:
            b.add (i**3)
    return len(b)

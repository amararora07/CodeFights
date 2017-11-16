from itertools import permutations

def isCube(n):
    i=1
    while i**3 <= n:
        if i**3==n:
            return True
        i+=1
    return False
    
def isSqure(n):
    return n == int(math.sqrt(n)) ** 2

def perfectSquareOrCube(n):
    s = str(n)
    c=0
    for i in list(set(permutations(str(s),len(s)))):
        x = int(''.join(i))
        print x,math.sqrt(x)
        if isCube(x) or isSqure(x):
            c+=1
    return c

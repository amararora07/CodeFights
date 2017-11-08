def leastFactorial(n):
    l=1
    while math.factorial(l) < n:
        l+=1
    return math.factorial(l)

def calculationsWithCoins(a, b, c):
    l={a,b,c,a+b,a+c,b+c,a+b+c}
    return len(l)

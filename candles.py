def candles(a,b):
    bu,l=0,0
    while a>0:
        bu+=a
        l+=a
        a=l/b
        l%=b
    return bu

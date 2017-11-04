def subtractionByRegrouping(m, s):
    a=s
    b=m-a
    c=[]
    while a+b>0:
        c.append(a%10+b%10)
        a /= 10
        b /= 10
    return c

def lastDigit(a, b):
    r=1
    for i in range(b):
        result = (result*a)%10
    return result

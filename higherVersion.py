def higherVersion(a, b):
    a = a.split('.')
    b = b.split('.')
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            return 1
        if int(a[i]) < int(b[i]):
            return 0
    return 0

def replaceAllDigitsRegExp(a):
    s=""
    for i in a:
        if '0'<=i<='9':
            s+='#'
        else:
            s+=i
    return s

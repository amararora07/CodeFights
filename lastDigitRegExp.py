def lastDigitRegExp(inp):
    l=[inp[i] for i in range(len(inp))]
    print l
    l=l[::-1]
    for i in l:
        if i.isdigit():
            return i

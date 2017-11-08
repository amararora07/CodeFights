def reflectString(inputString):
    s=""
    for i in range(len(inputString)):
        s+=chr(219-ord(inputString[i]))
    return s

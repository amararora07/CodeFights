def stolenLunch(n):
    s=""
    for i in range(len(n)):
        if 48<=ord(n[i])<=57:
            c=chr(ord(n[i])-48)
            s+=chr(ord(c)+97)
        elif 97<=ord(n[i])<=106:
            c=chr(ord(n[i])-97)
            s+=chr(ord(c)+48)
        else:
            s+=n[i]
    return s

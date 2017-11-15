def longestWord(text):
    s=""
    l=[]
    for i in range(len(text)):
        if 'a'<=text[i]<='z' or 'A'<=text[i]<='Z':
            l.append(text[i])
            if len(l)>len(s):
                s=''.join(l)
        else:
            del l[:]
    return s

def convolutedSummary(l):
    s=""
    for i in l.lower():
        if 'a'<=i<='e':
            s+=i.upper()
        elif 'v'<=i<='z':
            s+=i
    return s

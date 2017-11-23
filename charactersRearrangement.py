def charactersRearrangement(string1, string2):
    s1,s2=0,0
    for i in string1:
        s1+=ord(i)
    for i in string2:
        s2+=ord(i)
    return s1==s2

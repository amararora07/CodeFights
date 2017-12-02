from collections import Counter as c
def composeKPalindromes(s, k):
    if len(s)<k:
        return False
    d=c(s)
    l=sum(i%2 for i in d.values())
    if l<=k:
        return True
    return False

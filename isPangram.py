import string as a
def isPangram(s): 
    return set(a.lowercase).issubset(set(s.lower()))

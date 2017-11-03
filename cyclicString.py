def cyclicString(s):
    for i in range(1,len(s)+1):
        if s in s[:i]*len(s):
            return i

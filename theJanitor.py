def theJanitor(word):
    l=[0]*26
    t=word[::-1]
    s=set(word)
    for i in s:
        l[ord(i)-97]=len(word)-word.index(i)-t.index(i)
    return l

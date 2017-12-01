def buildPalindrome(st):
    a=lambda st:st[::-1]
    b=lambda st:st==a(str)
    for i in range(len(st)):
        if b(st[i:]):
            return st+a(st[:i])

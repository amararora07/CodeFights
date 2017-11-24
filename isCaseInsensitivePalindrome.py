def isCaseInsensitivePalindrome(inp):
    inp=inp.lower()
    return inp==inp[::-1]

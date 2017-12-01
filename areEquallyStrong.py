def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    a=[yourLeft, yourRight]
    b=[friendsLeft, friendsRight]
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def isPower(n):
    for i in range(1,100):
        for j in range(2,100):
            if i**j==n:
                return True
    return False

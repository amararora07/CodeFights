def isGeometricProgression(s):
    d = float(s[1]) / s[0]
    for i in range(2, len(s)):
        if d != float(s[i]) / s[i - 1]:
            return False
    return True

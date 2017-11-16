def latinLettersSearchRegExp(inp):
    for i in range(len(inp)):
        if inp[i].isalpha():
            return True
    return False

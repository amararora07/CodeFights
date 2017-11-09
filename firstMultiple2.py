def firstMultiple2(div, start):
    while 1:
        for i in range(len(div)):
            if start % div[i] == 0:
                return start
    start+=1

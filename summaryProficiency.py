def summaryProficiency(a, n, m):
    b,s=1,[]
    for i in a:
        if i >= m and b<=n:
            s.append(i)
        else:
            continue
        b+=1
    print s
    return sum(s)

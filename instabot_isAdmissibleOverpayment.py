def isAdmissibleOverpayment(prices, notes, x):
    amount=0
    i=0
    for i in range(len(prices)):
        l=tra(notes[i])
        c=prices[i]
        if l[0] != "Same":
            r = float( l[0].split("%")[0])*0.01
        if l[1] == "higher": 
            o=c/(1+r)
            amount+=(c-o)
        elif l[1] == "lower":
            o=c/(1-r)
            amount+=(c-o)
    if abs(x-amount)<0.0000001 or x>=amount:
        return True
    return False
def tra(p):
    pt=str(p)
    return pt.split(" ",2)

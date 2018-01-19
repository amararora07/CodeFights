def factorSum(n):
    def sumFact(n):
        t=2
        tot=0
        while n>1:        
            while n%t==0:
                tot+=t 
                n/=t 
            t+=1 
        return tot
    while n!=sumFact(n):
        n=sumFact(n)
    return n

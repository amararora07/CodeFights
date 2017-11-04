def sumOfPowers(n, divisor):
    l=0;
    for i in range(1,n+1):
        tmp=i;
        while tmp%divisor==0:
            tmp/=divisor 
            l+=1
    return l;

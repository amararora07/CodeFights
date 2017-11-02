def lateRide(n):
    if n>=0 and n<(60*24):
        a=n/60
        b=n%60
        return a/10+a%10+b/10+b%10

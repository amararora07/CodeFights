def circleOfNumbers(n, firstNumber):
    if n>=4 and n<=20 and firstNumber>=0 and firstNumber<=(n-1):
        return (firstNumber+n/2)%n

def replaceFirstDigitRegExp(input):
    s=""
    for i in input:
        if "#" in s:
            s+=i
            continue
        if "0"<=i<="9":
            s+="#"
        else:
            s+=i
    return s

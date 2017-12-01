def phoneCall(min1, min2, min11, s):
  if s<min1:
    return 0
  for i in range(2,11):
    if s<min1+min2*(i-1):
      return i-1
  return 10+(s-min1-min2*9)/min11

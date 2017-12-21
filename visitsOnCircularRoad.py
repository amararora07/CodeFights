def visitsOnCircularRoad(n, v):
    d,s=1,0
    for i in range(len(v)):
      s+=min(abs(v[i]-d),n-abs(v[i]-d))
      d=v[i]
    return s

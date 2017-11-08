def growingPlant(up, down, dh):
  c,d=0,1
  while c+up < dh:
    c+=up-down
    d+=1
  return d

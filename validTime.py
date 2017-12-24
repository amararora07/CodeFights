def validTime(t):
   hours=int(t[0]+t[1])
   minutes=int(t[3]+t[4])
   return hours<24 and minutes<60

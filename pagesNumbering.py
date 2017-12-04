def pagesNumbering(n):
  tp,dp,r=1,1,0
  while tp*10 <= n:
    r+=tp*9*dp
    tp*=10
    dp+=1
  r+=(n-tp+1)*dp
  return r

P = int(input())
Q = int(input())
R = int(input())
S = int(input())
dct = {}
maxl = 0
count = 0
def f(x,y):
  global count, maxl
  count += 1
  if x<y:
    x, y = y,x
  if x==0 or y==0:
    return 0
  if x==y:
    return 1
  else:
    if (x,y) not in dct:
      dct[(x,y)] = 1+f(x-y,y)
      if len(dct)>maxl: maxl = len(dct)
      if ((x-y,y) in dct): del dct[(x-y,y)]
    return dct[(x,y)]
res = 0
for i in range(P,Q+1):
  for j in range(R,S+1):
    res += f(i,j)
print(res)
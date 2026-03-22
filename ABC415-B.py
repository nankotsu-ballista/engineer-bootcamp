S=input()
N=len(S)
odd=0
for i in range(0,N):
  if S[i] =="#":
    if odd == 0:
      odd=1
      ta=i+1
    else:
      print(str(ta)+","+str(i+1))
      odd=0
  
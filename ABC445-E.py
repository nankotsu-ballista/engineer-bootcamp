import math
from collections import defaultdict
mod=998244353
# t=int(input())
# for i in range(t):
N = 10**7
factors=[-1]*(N+1)
for i in range(2,N):
  if factors[i]!=-1:
    continue
  else:
    for k in range(1,N//i+1):
      if factors[i*k]==-1:
        factors[i*k]=i
#print(factors)
t=int(input())
for _ in range(t):
  a=int(input())
  L=[int(a) for a in input().split()]
  factorcount=defaultdict(list)
  s=set()
  ansfactor=[[] for _ in range(a)]
  for i in range(a):
      num=L[i]
      tmpcount=defaultdict(int)
      while factors[num]!=-1:
        tmpcount[factors[num]]+=1
        num=num//factors[num]
      #print(tmpcount)
      for k, v in tmpcount.items():
        ansfactor[i].append((k,v))
        if k in s:
          factorcount[k].append(v)
          factorcount[k].sort()
          factorcount[k]=factorcount[k][1:]
        else:
          factorcount[k]=[0,v]
          s.add(k)
          
  ans=1
  for k, v in factorcount.items():
    ans=ans*(k**v[-1])%mod
  tmpans=ans
  anss=[]
  for i in range(a):
    tmpans=ans
    for k,v in ansfactor[i]:
      if factorcount[k][-1]==v:
        tmpans = tmpans * pow((k**(factorcount[k][-1]-factorcount[k][0])), mod-2, mod) % mod
    anss.append(tmpans%mod)
  print(*anss)
